import os
import shutil
source = input("enter your source folder:-")
destination = input("enter destination folder:-")
source = source+'/'
destination = destination+'/'
listoffiles = os.listdir(source)
for file in listoffiles :
    shutil.move((source+file),destination)