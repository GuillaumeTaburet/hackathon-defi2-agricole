import xarray as xr
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon
import folium


if __name__ == "__main__":

    # Objectif de l'indicateur :
    # Par période de 20 ans, nombre d’occurrence du dépassement du seuil 40°C ou 35°C 3 jours consécutifs entre avril et juin.
    ####### PARAMETRES ########
    nc_file_historique = "data/tasmaxAdjust_FR-Metro_CNRM-ESM2-1_historical_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_19500101-20141231.nc"
    nc_file = "data/tasmaxAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_20150101-21001231.nc"
    seuil_01 = 313.15  # K = 40°C

    # Boite Occitanie
    lat_min, lat_max = 42, 45.5
    lon_min, lon_max = -1, 5
    shapfile_mask = "shp_Occitanie/Occitanie_based_NUTS.shp"

    TRACC_dict = {
        "historique": 1970,
        "TRACC_01": 2042,
        "TRACC_02": 2062,
        "TRACC_03": 2081,
    }
    modele_name = "CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-ALADIN64E1_MF-CDFt-ANASTASIA-SAFRAN"
    ###########################

    for tracc, year in TRACC_dict.items():
        year_min = year - 10
        year_max = year + 9
        print(f"{tracc}: {year_min} – {year_max}")

        # 1️⃣ Lecture du netcdf
        if tracc == "historique":
            ds = xr.open_dataset(nc_file_historique, engine="netcdf4")
        else:
            ds = xr.open_dataset(nc_file, engine="netcdf4")
        tas = ds["tasmaxAdjust"]

        # 2️⃣ Sélection temporelle
        tas_sel = tas.sel(time=slice(f"{year_min}-01-01", f"{year_max}-12-31"))

        # 3️⃣ Sélection spatiale
        lat = ds["lat"].values
        lon = ds["lon"].values
        mask = (lat >= lat_min) & (lat <= lat_max) & (lon >= lon_min) & (lon <= lon_max)

        # 4️⃣ Calcul du nombre de jours > seuil
        occ_all = (tas_sel > seuil_01).sum(dim="time").values  # 2D (y,x)
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

        rows = [{"occ_above_40C": val / 20} for val in vals]
        # Création GeoDataFrame plus aisée pour folium
        gdf = gpd.GeoDataFrame(rows, geometry=geoms, crs="EPSG:4326")
        gdf = gdf.reset_index().rename(columns={"index": "id"})

        # Faire l'intersection avec le shapefile mask
        gdf_shp_mask = gpd.read_file(shapfile_mask)
        gdf = gpd.overlay(gdf, gdf_shp_mask, how="intersection")

        # 6️⃣ Carte Folium
        center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]
        m = folium.Map(location=center, zoom_start=7)

        # Tranches de la colorbar
        # thresholds = [0, 5, 10, 20, 50, 100, 500]
        # thresholds = [0, 100, 200, 300, 400, 500]
        thresholds = [0, 1, 2, 3, 4, 365]

        folium.Choropleth(
            geo_data=gdf.to_json(),
            data=gdf,
            columns=["id", "occ_above_40C"],
            key_on="feature.properties.id",
            fill_color="Reds",
            fill_opacity=0.7,
            line_opacity=0,
            nan_fill_color="white",
            legend_name=None,
            threshold_scale=thresholds,
        ).add_to(m)

        # Suppression FORCÉE de la légende Folium
        hide_legend_css = """
        <style>
        .leaflet-control.leaflet-control-legend, 
        .leaflet-legend, 
        .legend, 
        .colorbar, 
        div[style*="position: absolute"][style*="background"] {
            display: none !important;
        }
        </style>
        """
        m.get_root().html.add_child(folium.Element(hide_legend_css))

        # Infobulles folium
        folium.GeoJson(
            gdf,
            style_function=lambda x: {
                "fillOpacity": 0,
                "weight": 0,
                "color": "transparent",
            },
            tooltip=folium.GeoJsonTooltip(
                fields=["occ_above_40C"],
                aliases=["Nb jours par an > 40°C :"],
                localize=True,
            ),
        ).add_to(m)

        # Supprimer la colorbar générée par Folium
        for child in list(m._children):
            if child.startswith("color_map"):
                del m._children[child]
        # Légende HTML personnalisée avec segments égaux
        legend_html = """
        <div style="
            position: fixed;
            bottom: 30px;
            left: 30px;
            width: 140px;
            background-color: white;
            padding: 10px;
            border: 2px solid grey;
            z-index: 9999;
            font-size: 13px;
        ">
        <b>Nombre de jours par an &gt; 40°C</b><br>
        <i style='background: #fee5d9; width: 18px; height: 12px; float: left; margin-right: 8px;'></i>0–1<br>
        <i style='background: #fcbba1; width: 18px; height: 12px; float: left; margin-right: 8px;'></i>1–2<br>
        <i style='background: #fc9272; width: 18px; height: 12px; float: left; margin-right: 8px;'></i>2–3<br>
        <i style='background: #fb6a4a; width: 18px; height: 12px; float: left; margin-right: 8px;'></i>3–4<br>
        <i style='background: #cb181d; width: 18px; height: 12px; float: left; margin-right: 8px;'></i>&gt;4<br>
        </div>
        """
        m.get_root().html.add_child(folium.Element(legend_html))

        # Titre de la figure (ajout html)
        title_html = f"""
        <h3 align="center" style="font-size:16px">
            Indicateur canicule : nombre de jours par an avec température maximale supérieurs à 40°C
        </h3>
        <h3 align="center" style="font-size:14px">
            {tracc} : {year_min} – {year_max}
        </h3>
        <p align="center" style="font-size:14px">
            Modèle RCM : {modele_name}
        </p>
        """
        m.get_root().html.add_child(folium.Element(title_html))

        # Sauvegarde du html
        m.save(f"02_indicateur-chaleur_{tracc}.html")
