import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Point
import fiona

#this function assumes the csv has a column named "Longitude" and "Latitude"
def csv_to_shp(csv, outname):
    df = pd.read_csv(csv)
    geom = [Point(xy) for xy in zip(df.Longitude, df.Latitude)]
    crs = {'init': 'epsg:4326'}
    geo_df = GeoDataFrame(df, crs=crs, geometry=geom)
    geo_df.to_file(driver='ESRI Shapefile', filename=("{}.shp".format(outname)))

# A test csv file with many columns including "Longitude" and "Latitude"
test_csv = 'points.csv'

#calling the function will convert 'points.csv', including all columns, to 'points.shp' in WGS84
csv_to_shp(test_csv, "points")