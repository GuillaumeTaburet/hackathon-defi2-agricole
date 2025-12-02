import xarray as xr
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon
import folium


if __name__ == "__main__":

    ####### PARAMETRES ########
    nc_file = "data/tasminAdjust_FR-Metro_CMCC-CM2-SR5_ssp370_r1i1p1f1_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_20150101-21001231.nc"
    seuil_01 = 261.15  # K = -12°C
    seuil_02 = 266.15  # K = -7°C

    # Boite Occitanie
    lat_min, lat_max = 42, 45
    lon_min, lon_max = -1, 3.5
    TRACC_dict = {"TRACC_01": 2033, "TRACC_02": 2050, "TRACC_03": 2072}
    ###########################

    for tracc, year in TRACC_dict.items():
        year_min = year - 10
        year_max = year + 9
        print(f"{tracc}: {year_min} – {year_max}")

        # 1️⃣ Lecture du netcdf
        ds = xr.open_dataset(nc_file, engine="netcdf4")
        tas = ds["tasminAdjust"]

        # 2️⃣ Sélection temporelle
        tas_sel = tas.sel(time=slice(f"{year_min}-01-01", f"{year_max}-12-31"))

        # 3️⃣ Sélection spatiale
        lat = ds["lat"].values
        lon = ds["lon"].values
        mask = (lat >= lat_min) & (lat <= lat_max) & (lon >= lon_min) & (lon <= lon_max)

        # 4️⃣ Calcul du nombre de jours < seuil
        occ_all = (tas_sel < seuil_01).sum(dim="time").values  # 2D (y,x)
        occ_all_masked = np.where(mask, occ_all, np.nan)  # ne garder que lla sélection

        # 5️⃣ Construction GeoDataFrame vectorisée
        lat_b = ds["lat_bnds"].values
        lon_b = ds["lon_bnds"].values

        y_inds, x_inds = np.where(~np.isnan(occ_all_masked))  # pixels valides
        vals = occ_all_masked[y_inds, x_inds].astype(int)

        # Construction des géométries de la grille
        geoms = [
            Polygon([(lon_b[j, i, k], lat_b[j, i, k]) for k in range(lat_b.shape[2])])
            for j, i in zip(y_inds, x_inds)
        ]

        rows = [{"occ_below_-12C": val} for val in vals]
        # Création GeoDataFrame plus aisée pour folium
        gdf = gpd.GeoDataFrame(rows, geometry=geoms, crs="EPSG:4326")
        gdf = gdf.reset_index().rename(columns={"index": "id"})

        # 6️⃣ Carte Folium
        center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]
        m = folium.Map(location=center, zoom_start=7)

        # Tranches de la colorbar
        thresholds = [0, 5, 10, 20, 50, 100, 300]

        folium.Choropleth(
            geo_data=gdf.to_json(),
            data=gdf,
            columns=["id", "occ_below_-12C"],
            key_on="feature.properties.id",
            fill_color="Reds",
            fill_opacity=0.7,
            line_opacity=0,
            nan_fill_color="white",
            legend_name="Nombre de jours < -12°C (2023–2043)",
            threshold_scale=thresholds,
        ).add_to(m)

        # Infobulles folium
        folium.GeoJson(
            gdf,
            style_function=lambda x: {
                "fillOpacity": 0,
                "weight": 0,
                "color": "transparent",
            },
            tooltip=folium.GeoJsonTooltip(
                fields=["occ_below_-12C"], aliases=["Nb jours < -12°C :"], localize=True
            ),
        ).add_to(m)

        # Titre de la figure (ajout html)
        title_html = f"""
        <h3 align="center" style="font-size:16px">
            Indicateur de gel : nombre de jours avec température minimale inférieure à -12°C
        </h3>
        <p align="center" style="font-size:14px">
            {tracc} : {year_min} – {year_max}
        </p>
        <p align="center" style="font-size:14px">
            Modèle GCM : CMCC-CM2-SR5
        </p>
        """
        m.get_root().html.add_child(folium.Element(title_html))

        # Sauvegarde du html
        m.save(f"01_indicateur-gel_{tracc}.html")
