#The following script converts a file from geopackage to shapefile format


import geopandas as gpd
import os

# ---- USER INPUT ----
input_folder = r"/path/to/your/gpkg_files"
output_folder = r"/path/to/output_shapefiles"

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all gpkg files
for file in os.listdir(input_folder):
    if file.lower().endswith(".gpkg"):
        gpkg_path = os.path.join(input_folder, file)
        base_name = os.path.splitext(file)[0]

        # Get all layers inside the geopackage
        layers = gpd.io.file.fiona.listlayers(gpkg_path)

        print(f"\nProcessing {file}...")
        for layer in layers:
            print(f"  - Converting layer: {layer}")

            # Read the layer
            gdf = gpd.read_file(gpkg_path, layer=layer)

            # Construct output shapefile name
            shp_name = f"{base_name}_{layer}.shp".replace(" ", "_")
            shp_path = os.path.join(output_folder, shp_name)

            # Write as shapefile
            gdf.to_file(shp_path)

        print(f"Finished {file}.")
