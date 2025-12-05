#The following script converts a file from geopackage to shapefile format


import geopandas as gpd
import os

# ---- USER INPUT ----
input_folder = r"/path/to/your/gpkg_files"
output_folder = r"/path/to/output_shapefiles"

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Check to see if GPKG files have more than one layer (this script is for .gpkg files with one layer)
for file in os.listdir(input_folder):
    if file.lower().endswith(".gpkg"):
        gpkg_path = os.path.join(input_folder, file)
        print(file, "→ layers:", fiona.listlayers(gpkg_path))

# Loop through .gpkg files in input folder and convert to .shp 
for file in os.listdir(input_folder):
    if file.lower().endswith(".gpkg"):
        gpkg_path = os.path.join(input_folder, file)
        base_name = os.path.splitext(file)[0]

        # There is only ONE layer in each geopackage
        layer = fiona.listlayers(gpkg_path)[0]

        print(f"\nProcessing {file}... (layer: {layer})")

        # Read the only layer
        gdf = gpd.read_file(gpkg_path, layer=layer)

        # Output shapefile uses only the GPKG base name
        shp_name = f"{base_name}.shp"
        shp_path = os.path.join(output_folder, shp_name)

        gdf.to_file(shp_path, driver="ESRI Shapefile")

        print(f"Finished {file}. → {shp_name}")
