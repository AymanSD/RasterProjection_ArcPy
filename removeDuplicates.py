import os

dir_name = r"C:\cc\sudanEra5Data1Tiff\in"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".tiff") or item.endswith(".xml"):
        os.remove(os.path.join(dir_name, item))
 
