import os
import arcpy
from arcpy import env

env.overwrite = True
##env.workspace = r"C:\cc\sudanEra5Data1Tiff"
##env.workspace = r"\\192.168.14.106\SudanWindAtlas2018\Sudan"
env.workspace = r"D:\GIS\Landsat"
folders = arcpy.ListWorkspaces("*","Folder")
os.mkdir(r"D:\GIS\Landsat_Projected")

for folder in folders:
    env.workspace = folder
    rasterFolder = os.path.basename(folder)                         # Retrieving the Sub folders name
    dirpath = r"D:\GIS\Landsat_Projected" + "/" + rasterFolder      # Path for new Directory      
    createSubdir = os.mkdir(dirpath)                                # Creating the new directory
    outFolder = r"D:\GIS\Landsat_Projected" + "/" + rasterFolder    # Path for the output folder for each raster
    a = arcpy.ListRasters()
##    print rasterFolder
##    print outFolder
    
    
    for b in a:
        c = b.split(".")[0]
##        print folder
##        print outFolder
##        print b;
##        print c
        
##        arcpy.ProjectRaster_management(b, folder + '/' + c + ".tif","32635") # UTM Zone35
        arcpy.ProjectRaster_management(b, outFolder + '/' + c + ".tif","3857")  # Web mercator      

