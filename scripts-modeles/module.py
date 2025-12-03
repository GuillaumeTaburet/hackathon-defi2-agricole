from pathlib import Path
import xarray as xr
import numpy as np
import pandas as pd

from explore4 import lat_min, lon_max, lon_min


# ============================================================
# ========== CALCULS ET0 — 3 MÉTHODES ========================
# ============================================================

def et0_fao56_simple(tmin, tmax, tmoy, huss, rlds, rsds, altitude):
    """Version simplifiée du FAO-56 (déjà utilisée)."""
    T = tmoy
    P = pressure_from_altitude(altitude)
    delta = slope_saturation_curve(T)
    es = saturation_vapor_pressure(T)
    ea = actual_vapor_pressure(huss, P)
    gamma = psychrometric_constant(P)
    Rn = rsds - rlds
    u2 = 2.0

    num = (0.408 * delta * Rn) + (gamma * (900. / (T + 273.)) * u2 * (es - ea))
    den = delta + gamma * (1 + 0.34 * u2)
    return num / den


def et0_hargreaves(tmin, tmax, tmoy, lat_rad, doy):
    """Hargreaves-Samani."""
    Ra = 37.6 * np.cos(lat_rad)  # approximation très grossière
    return 0.0023 * (tmoy + 17.8) * np.sqrt(tmax - tmin) * Ra


def et0_fao56_complet(tmin, tmax, tmoy, huss, rlds, rsds, altitude, u2):
    """
    Version complète FAO-56 recommandée.
    Nécessite u2 (vent)
    """
    T = tmoy
    P = pressure_from_altitude(altitude)
    delta = slope_saturation_curve(T)
    es = saturation_vapor_pressure(T)
    ea = actual_vapor_pressure(huss, P)
    gamma = psychrometric_constant(P)

    # FAO: Rns = 0.77 * Rs
    Rns = 0.77 * rsds

    # Rayonnement net long-onde FAO-56 Eq 39
    sigma = 4.903e-9
    t_k4 = ((tmax + 273.16)**4 + (tmin + 273.16)**4) / 2
    Rnl = sigma * t_k4 * (0.34 - 0.14 * np.sqrt(ea)) * (1.35 * (rsds / (0.75)) - 0.35)

    Rn = Rns - Rnl

    num = 0.408 * delta * Rn + gamma * (900 / (T + 273)) * u2 * (es - ea)
    den = delta + gamma * (1 + 0.34 * u2)
    return num / den


# ===========================================================
# =============== CLASSE RCMmodel ============================
# ===========================================================

class RCMmodel:
    def __init__(self, name, simu,step_years=20, et0_method="FAO56_simple"):
        self.name = name
        self.simu = simu
        self.tracc = self.get_tracc(name, simu)
        self.et0_method = et0_method        # <-- methode de ET0

        self.output_dir = Path("./indicateurs") / f"{name}_{simu}"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        VARIABLES = ['huss', 'pr', 'rlds', 'rsds', 'sfcWind', 'tas', 'tasmin', 'tasmax']
        lon_min, lat_min, lon_max, lat_max = -0.3271761354085185, 42.3329214736443120, 4.8455688506624455, 45.0466746429150078

        # -------------------------------
        # 🎯 Attribut Dictionnaire Final
        # self.values[var][t_key] = dataset croppé
        # -------------------------------
        self.values = {var: {} for var in self.VARIABLES}

    # ---------------------------------------------------------
    # Chargement + crop + stockage dans self.values
    # ---------------------------------------------------------
    def load_and_crop(self):

        for var in self.VARIABLES:

            # --------------------------------------------
            # 1) Ouvre le fichier NetCDF associé
            # --------------------------------------------
            file_path = f"/home/carole/Téléchargements/{var}Adjust_{self.name}_{self.simu}_ALADIN64E1.nc"
            print(f"📂 Chargement : {file_path}")
            ds = xr.open_dataset(file_path)

            # --------------------------------------------
            # 2) Crop spatial
            # --------------------------------------------
            ds = self.crop_spatial(ds, lat_max= 45.0466746429150078, lat_min=42.3329214736443120, lon_max=4.8455688506624455, lon_min=-0.3271761354085185)

            # --------------------------------------------
            # 3) Crop temporel + stockage dans self.values
            # --------------------------------------------
            for t_key, time_sel in self.tracc.items():
                print(f"   ↳ période t{t_key} : {time_sel}")

                # crop temporel : time_sel = {"start": "...", "end": "..."}
                ds_t = crop_time(ds, time_sel)

                # 🎯 Stockage dans le dictionnaire
                self.values[var][f"t{t_key}"] = ds_t


    # ------------------------------------------
    # --- CROP ESPACE
    # ------------------------------------------
    def crop_spatial(self, ds, lat_max, lat_min, lon_min, lon_max):
        return ds.sel(lat=slice(lat_max, lat_min), lon=slice(lon_min, lon_max))

    # ------------------------------------------
    # --- SELECTEUR TEMPOREL A PAS DE N ANS
    # ------------------------------------------
    def get_tracc(self):
        if self.simu == "histo" :
            return{'t1' : 1995}
        elif self.name == "NorESM2-MM" :
            return {'t1' : 2040, 't2' : 2059, 't3' : 2079}
        elif self.name == "CNRM-ESM2-1"
            return {'t1' : 2042, 't2' : 2062, 't3' : 2081}

    def year_selection(self, year):
        """
        A partir de time_sel définir la fenêtre temporelle avec y_start à n-10 
        et y_end à n+9 pour faire une selection sur le data set (ds)
        """
             
        y_start = self.tracc[i] - 10
        y_end = self.tracc[i] + 9
        
        tracc_sel = ds.sel(time=slice(f"{y_start}-01-01", f"{year_end}-12-31"))


    # -------------------------------------------------------------
    # -------------------- INDICATEUR ET0 -------------------------
    # -------------------------------------------------------------
    def indicateur_evapotranspiration(self, time, tmin, tmax, tmoy, huss, rlds, rsds,
                                      altitude, u2=None, lat=None):

        method = self.et0_method

        if method == "FAO56_simple":
            et0 = et0_fao56_simple(tmin, tmax, tmoy, huss, rlds, rsds, altitude)

        elif method == "FAO56_complet":
            if u2 is None:
                raise ValueError("Méthode FAO56_complet nécessite une variable u2 (vent).")
            et0 = et0_fao56_complet(tmin, tmax, tmoy, huss, rlds, rsds, altitude, u2)

        elif method == "Hargreaves":
            lat_rad = np.radians(lat)
            doy = pd.DatetimeIndex(time).dayofyear.values
            et0 = et0_hargreaves(tmin, tmax, tmoy, lat_rad, doy)

        else:
            raise ValueError("Méthode ET0 inconnue.")

        # NetCDF annuel
        ti = pd.DatetimeIndex(time)
        years = np.unique(ti.year)
        values = []

        for y in years:
            mask = (ti.year == y)
            values.append(et0[mask].sum())

        ds = xr.Dataset(
            {"ET0": (("year",), values)},
            coords={"year": years}
        )

        ds.to_netcdf(self.output_dir / "ET0_annuel.nc")
        return ds, et0

    # -------------------------------------------------------------
    # ----------------------- AUTRES INDICATEURS -----------------
    # -------------------------------------------------------------

    # Tous les autres indicateurs suivent la même structure
    # (sortie NetCDF)

    # ----- FROID EXTREME -------
    def indicateur_froid_extreme(self, time, tmin):
        ti = pd.DatetimeIndex(time)
        years = np.unique(ti.year)
        out = []

        for y in years:
            mask = (ti >= f"{y}-11-01") | (ti <= f"{y}-02-28")
            t = tmin[mask]
            cold = int((t < -12).sum() > 0 or (t < -7).sum() >= 5)
            out.append(cold)

        ds = xr.Dataset({"froid_extreme": (("year",), out)},
                        coords={"year": years})
        ds.to_netcdf(self.output_dir / "froid_extreme.nc")
        return ds

    # ----- CHALEUR EXTREME AMJ -------
    def indicateur_chaleur_extreme(self, time, tmax):
        ti = pd.DatetimeIndex(time)
        years = np.unique(ti.year)
        out = []

        for y in years:
            mask = (ti >= f"{y}-04-01") & (ti <= f"{y}-06-30")
            tx = tmax[mask]
            cond = (tx > 40).any() or np.any((tx[:-2]>35)&(tx[1:-1]>35)&(tx[2:]>35))
            out.append(int(cond))

        ds = xr.Dataset({"chaleur_extreme": (("year",), out)},
                        coords={"year": years})
        ds.to_netcdf(self.output_dir / "chaleur_extreme_AMJ.nc")
        return ds

    # ----- DEFICIT HYDRIQUE -------
    def indicateur_deficit_hydrique(self, time, et0, precip):
        ti = pd.DatetimeIndex(time)
        years = np.unique(ti.year)
        out = []

        deficit = np.maximum(0, et0 - precip)

        for y in years:
            mask = (ti >= f"{y}-06-01") & (ti <= f"{y}-08-31")
            out.append(int(deficit[mask].sum() > 100))

        ds = xr.Dataset({"deficit_hydrique": (("year",), out)},
                        coords={"year": years})
        ds.to_netcdf(self.output_dir / "deficit_hydrique_JJA.nc")
        return ds

    # ----- FRAICHEUR HIVER -------
    def indicateur_fraicheur_hiver(self, time, tmin, tmax):
        ti = pd.DatetimeIndex(time)
        years = np.unique(ti.year)
        out = []

        tm = (tmin + tmax) / 2
        for y in years:
            mask = (ti >= f"{y}-11-01") | (ti <= f"{y}-02-28")
            out.append(int((tm[mask] <= 12).sum() < 70))

        ds = xr.Dataset({"fraicheur_hiver": (("year",), out)},
                        coords={"year": years})
        ds.to_netcdf(self.output_dir / "fraicheur_hiver.nc")
        return ds

    # -------------------------------------------------------------
    # ----------------------- PROCESS ALL -------------------------
    # -------------------------------------------------------------
    def process_all(self, time, tmin, tmax, tmoy, huss, rlds, rsds,
                    precip, altitude, sfcWind, lat=None):

        et0_annuel, et0_journalier = self.indicateur_evapotranspiration(
            time, tmin, tmax, tmoy, huss, rlds, rsds, altitude,
            u2=u2, lat=lat
        )

        return {
            "ET0": et0_annuel,
            "froid": self.indicateur_froid_extreme(time, tmin),
            "chaleur": self.indicateur_chaleur_extreme(time, tmax),
            "deficit": self.indicateur_deficit_hydrique(time, et0_journalier, precip),
            "fraicheur": self.indicateur_fraicheur_hiver(time, tmin, tmax),
        }
