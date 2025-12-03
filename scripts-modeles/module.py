from pathlib import Path
import xarray as xr
import numpy as np
import pandas as pd


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

        if self.simu == "histo" :
            self.values = {}

    def load_and_crop(self):
        for var in VARIABLES :
            ds = xr.open_dataset(f"/home/carole/Téléchargements/{var}Adjust_{self.name}_{self.simu}_ALADIN64E1.nc")
            ds = crop_spatial(ds)
                for year in self.tracc.keys() :
                    ds = crop_time(ds, self.tracc[year])
                save ds in variable names after the variable and the tracc key for example huss_t1


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

    def crop_1_year_every_N_years(self, year):
        """
        Conserve 1 année représentative tous les X ans.
        Exemple : step_years=20 -> on garde 1960, 1980, 2000, etc.
        A changer pour renvoyer un masque correspondant aux onnées dela tracc spécifique du model. enargumentprend une option t1, t2 ou t3 qui sont es 3 step de la tracc
        """
        years = np.unique(ds.time.dt.year.data)

        selected_years = []
        start = years.min()
        end = years.max()

        for yr in range(start, end + 1, self.step_years):
            selected_years.append(yr)

        mask = ds.time.dt.year.isin(selected_years)
        return ds.sel(time=mask)

    # ------------------------------------------
    # --- Chargement + traitement générique
    # ------------------------------------------
    import requests
    from pathlib import Path
    import re

    def download_variable(self, varname, dest_dir):
        """
        Télécharge automatiquement le seul fichier NetCDF présent dans :
            <model_url>/<varname>Adjust/version-hackathon-102025/
        """

        # Construire l'URL du répertoire en ligne
        url = f"{self.model_url}{varname}Adjust/version-hackathon-102025/"

        dest_dir = Path(dest_dir)
        dest_dir.mkdir(parents=True, exist_ok=True)

        # 1) Télécharger la page HTML listant les fichiers
        r = requests.get(url)
        if r.status_code != 200:
            raise ConnectionError(f"Impossible d'accéder à l'URL : {url}")

        html = r.text

        # 2) Trouver le lien vers le fichier .nc unique
        matches = re.findall(r'href="([^"]+\.nc)"', html)

        if len(matches) == 0:
            raise FileNotFoundError(f"Aucun fichier .nc trouvé dans : {url}")

        if len(matches) > 1:
            raise RuntimeError(
                f"Plusieurs fichiers .nc trouvés, mais un seul était attendu : {matches}")

        filename = matches[0]
        file_url = url + filename

        # 3) Chemin local
        local_path = dest_dir / filename

        # 4) Téléchargement du fichier
        print(f"Téléchargement : {file_url}")
        with requests.get(file_url, stream=True) as req:
            req.raise_for_status()
            with open(local_path, "wb") as f:
                for chunk in req.iter_content(chunk_size=8192):
                    f.write(chunk)

        print(f"Fichier téléchargé : {local_path}")

        return local_path

    def process_variable(self, varname, dataset="safran",
                                  lat_max=None, lat_min=None,
                                  lon_min=None, lon_max=None):
        """ varname among : "huss", "pr", "rlds", "rsds", "sfcWind", "tas", "tasmax", "tasmin" """

        fpath = self.model_url + varname+"Adjust/version-hackathon-102025/*"
        ds = xr.open_dataset(fpath)[[varname]]

        if lat_max is not None:
            ds = self.crop_spatial(ds, lat_max, lat_min, lon_min, lon_max)

        ds = self.crop_1_year_every_N_years(ds)
        return ds

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
