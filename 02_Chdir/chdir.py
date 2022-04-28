import os
import shutil

rootPath= "E:\\video\\Bilibili Download\\BV1zp4y1i75g-fluent工程实例教程"

for item in os.listdir(rootPath):
    for file in os.listdir(rootPath+"\\"+item):
        if ".mp4" in os.path.basename(file):
            # print("renaming"+rootPath+"\\"+item+"\\"+os.path.basename(file)+" to "+rootPath+"\\"+os.path.basename(file))
            os.rename(rootPath+"\\"+item+"\\"+os.path.basename(file), rootPath+"\\"+os.path.basename(file))
            shutil.rmtree(rootPath+"\\"+item)
            # print("removing "+rootPath+"\\"+item)