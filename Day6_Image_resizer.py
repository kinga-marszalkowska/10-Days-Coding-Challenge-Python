from os import listdir
from os.path import isfile, join
import os
from tkinter import filedialog
from tkinter import *
from PIL import Image

# open window for choosing file folder
root = Tk()
root.withdraw()
path_to_image_folder = filedialog.askdirectory()

# open window to choose outpput file folder
root.withdraw()
path_to_output_folder = filedialog.askdirectory()

# get all the files from a folder
image_paths = []
image_filenames = []
size_before = []
size_after = []

# get paths to all images
for f in listdir(path_to_image_folder):
    if isfile(join(path_to_image_folder, f)):
        image_paths.append(join(path_to_image_folder, f))
        image_filenames.append(f)

# resize images
for i in range(len(image_paths)):
    image = Image.open(image_paths[i])
    size = image.size
    # get size of an image before conversion convert bytes to mb
    size_before.append(os.stat(image_paths[i]).st_size / 100000)
    # resize image, to 75% of its original dimensions
    image = image.resize((int(size[0] * 0.75), int(size[1] * 0.75)), Image.ANTIALIAS)
    image.save(join(path_to_output_folder, image_filenames[i]), optimize=True, quality=70)
    # get size of an image after conversion
    size_after.append(os.stat(join(path_to_output_folder, image_filenames[i])).st_size / 100000)
    print(image_paths[i], "{:.1f}".format(size_before[i]), "{:.1f}".format(size_after[i]))

# calculate saved space
total_size_before = sum(size_before)
total_size_after = sum(size_after)

saved_space = total_size_before - total_size_after

print("Before conversion: {before}mb, after conversion {after}mb, saved space: {saved}mb, {saved_percent}%".format(
    before="{:.1f}".format(total_size_before),
    after="{:.1f}".format(total_size_after),
    saved="{:.1f}".format(saved_space),
    saved_percent="{:.1f}".format(100 - ((saved_space / total_size_before) * 100))
))
