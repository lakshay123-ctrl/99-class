import os
import shutil
path = "/Users/lenovo/desktop/movies"
print("before moving file:")
source = "/Users/lenovo/desktop/movies/tur.png"
destination = "/Users/lenovo/desktop/desktop"
dest = shutil.move(source,destination)
print("files moved")
