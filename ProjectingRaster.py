## This code is utilised to project raster data 
## Required Libraries: os, arcpy
## Parameters: raster directory, output directory, Map Projection
## Author: Ayman Altoum
## Date:26. July. 2019

import os
import arcpy
from arcpy import env

# Defining Workspace:
env.overwrite = True
env.workspace = r"D:\GIS\Landsat"

# Obtaining a list of directories within the workspace
folders = arcpy.ListWorkspaces("*","Folder")
os.mkdir(r"D:\GIS\Landsat_Projected")

for folder in folders:
    env.workspace = folder
    rasterFolder = os.path.basename(folder)                         # Retrieving the Sub folders name
    dirpath = r"D:\GIS\Landsat_Projected" + "/" + rasterFolder      # Path for new Directory      
    createSubdir = os.mkdir(dirpath)                                # Creating the new directory
    outFolder = r"D:\GIS\Landsat_Projected" + "/" + rasterFolder    # Path for the output folder for each raster
    a = arcpy.ListRasters()
    
## Projecting Rasters:
    for b in a:
        c = b.split(".")[0]
        arcpy.ProjectRaster_management(b, outFolder + '/' + c + ".tif","3857")  # Web mercator      

