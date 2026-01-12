from src.api import fetch_all_features
from src.process import process_roads

def main():
    gdf = fetch_all_features()
    gdf = process_roads(gdf)

    return gdf

if __name__ == "__main__":
    output = main()
    output.to_file("data/OUT/temp_output.geojson", driver="GeoJSON")