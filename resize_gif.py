#by Fredray-21
from PIL import Image, ImageSequence
import os, sys
from pathlib import Path

# Wrap on-the-fly thumbnail generator
def thumbnails(frames):
    for frame in frames:
        thumbnail = frame.copy()
        thumbnail.thumbnail(size, Image.ANTIALIAS)
        yield thumbnail

        
# Output (max) size
x = int(input("Size: "))

size = x,x
# Open a file

name_path = input("Name File: ")
path = "./"+name_path+"/"

name_file = os.path.exists("./"+name_path+"_resize"+str(x)+"x"+str(x))
if (name_file == False):
    os.makedirs(name_path+"_resize"+str(x)+"x"+str(x))

dirs = os.listdir(path)
for file in dirs:
    if(file.split(".")[1] =="gif"):
        name = file.split(".")[0]
        print(file)
        # Open source
        im = Image.open(path+file)
        # Get sequence iterator
        frames = ImageSequence.Iterator(im)
        frames = thumbnails(frames)
        # Save output
        om = next(frames) # Handle first frame separately
        om.save("./"+name_path+"_resize"+str(x)+"x"+str(x)+"/"+name+"_resize.gif", save_all=True, append_images=list(frames),disposal=2)
