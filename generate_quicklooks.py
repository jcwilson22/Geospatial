import os
import processing
from qgis.core import QgsProject, QgsRasterLayer

# Set output folder path 
output_folder = r"/your/output/folder"  # <-- Paste file path here

#Define three bands to be used in quicklooks
RED_BAND = 78
GREEN_BAND = 46
BLUE_BAND = 15

# Make sure the output directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop over all raster layers
for layer in QgsProject.instance().mapLayers().values():
    if isinstance(layer, QgsRasterLayer) and layer.providerType() == 'gdal':
        print(f"Processing: {layer.name()}")

        input_path = layer.source()
        base_name = layer.name().replace(" ", "_")
        output_path = os.path.join(output_folder, f"{base_name}_RGB.tif")

        # Use gdal:translate with -b parameters for band selection
        params = {
            'INPUT': input_path,
            'NODATA': None,
            'COPY_SUBDATASETS': False,
            'OPTIONS': '',
            'EXTRA': f'-b {RED_BAND} -b {GREEN_BAND} -b {BLUE_BAND}',
            'DATA_TYPE': 0,  # Same as input
            'OUTPUT': output_path
        }

        result = processing.run("gdal:translate", params)

        print(f"Saved RGB image to: {output_path}")