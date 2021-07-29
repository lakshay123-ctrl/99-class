import os
import shutil
path = "/Users/lenovo/desktop"
print("before copying file:")
print(os.listdir(path))
source = "/Users/lenovo/desktop/py.txt"
destination = "/Users/lenovo/desktop/movies/pycopy.txt"
dest = shutil.copy(source,destination)
print("after copying file")
print(os.listdir(path))