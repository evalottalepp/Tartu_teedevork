import requests
import pandas as pd
import geopandas as gpd

def fetch_all_features() -> gpd.GeoDataFrame:
    base_url = "https://gis.tartulv.ee/arcgis/rest/services/Liikluskorraldus/LI_teed/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"

    params = {
        "f": "geojson",
        "returnGeometry": "true",
        "resultOffset": 0,
        "resultRecordCount": 1000
        }

    all_features = []

    while True:
        r = requests.get(base_url, params=params)
        if r.status_code != 200 or 'features' not in r.json():
            break

        gdf = gpd.read_file(r.text)
        all_features.append(gdf)

        if len(gdf) < params["resultRecordCount"]:
            break

        params["resultOffset"] += params["resultRecordCount"]

    full_gdf = pd.concat(all_features, ignore_index=True)
    
    return full_gdf