# 1. Clipi Tartu piiriga teed ära
# 2. Jäta alles valikulised tulbad
# 3. Tõlgi integerid loogilisteks väärtusteks mapperfunktsioonidega
# 4. Lisa teedele liiklusmahud ja kiirused

import pandas as pd
import geopandas as gpd

def process_roads(all_roads_gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    clipped_roads = clip_to_tartu_boundary(all_roads_gdf)
    return clipped_roads


def clip_to_tartu_boundary(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        # Load Tartu boundary shapefile
        tartu_boundary = gpd.read_file("data/IN/tartu.geojson")
        tartu_boundary = tartu_boundary.to_crs(gdf.crs)

        # Clip roads to Tartu boundary
        clipped_gdf = gpd.clip(gdf, tartu_boundary)
        return clipped_gdf


def rename_columns(gdf: gpd.GeoDataFrame, columns_map: dict) -> gpd.GeoDataFrame:
    gdf = gdf.rename(columns=columns_map)
    return gdf


def read_mapper(file_path: str) -> dict:
    df = pd.read_csv(file_path)
    mapper = dict(zip(df["code"], df["value"]))
    return mapper

if __name__ == "__main__":
    pass