# -*- coding: utf-8 -*-
"""TIFF_to_ENVI.ipynb
Code to take DEMs generated in GEE (geotiff) to ENVI.hdr format
"""

import os
from osgeo import gdal

"""Mount Google Drive to get access to DEM files"""

#Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

"""Create a conversion function"""

def convert_geotiff_to_envi(input_folder, output_folder):
  """Converts all GeoTIFF fiels in the input folder to ENVI format"""
  for file_name in os.listdir(input_folder):
    if file_name.endswith('.tif'):
      input_file_path = os.path.join(input_folder, file_name)
      output_file_path = os.path.join(output_folder, file_name.replace(".tif",""))

      try:
        dataset = gdal.Open(input_file_path)
        driver = gdal.GetDriverByName('ENVI')
        driver.CreateCopy(output_file_path, dataset)
        dataset.FlushCache()
        print(f"Converted {file_name} to ENVI format.")
      except Exception as e:
        print(f"Error converting {file_name} to ENVI format.")


#set the input and output folders
input_folder = "/content/drive/MyDrive/Townsend_Lab/DEM/GeoTIFF"
output_folder = "/content/drive/MyDrive/Townsend_Lab/DEM/ENVI"

"""Now use your function to convert GeoTiffs to ENVI header files."""

convert_geotiff_to_envi(input_folder, output_folder)
