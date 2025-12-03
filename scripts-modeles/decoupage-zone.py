import xarray as xr
import geopandas as gpd

ds = xr.open_dataset(path)

df = ds.to_dataframe().reset_index()

#Ajout de la colonne de géométrie
df['geometry'] = df.apply(lambda row: Point(row['lon'], row['lat']), axis=1)

gdf= gpd.GeoDataFrame(df, geometry='geometry')

#import de l’emprise
extent = gpd.read_file(“path/to/.shp”)

#découpage 

crop_gdf = gpd.sjoin(gdf,extent,how="inner", op='intersects')
