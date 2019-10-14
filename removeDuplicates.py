## This code is utilised to remove duplicate raster data 
## Required Libraries: os, arcpy
## Parameters: raster directory, raster extension
## Author: Ayman Altoum
## Date:26. July. 2019


import os

dir_name = r"C:\cc\sudanEra5Data1Tiff\in"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".tiff") or item.endswith(".xml"):
        os.remove(os.path.join(dir_name, item))
 
