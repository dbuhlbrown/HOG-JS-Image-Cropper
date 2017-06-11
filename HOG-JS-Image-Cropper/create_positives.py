#This file just creates a positive.txt text file which contains the image names (with full paths)
#That can be used with the hog_cropper file

import glob
import os
import re

positive_images_direcotry = "positive_images"
positive_image_file = "positive.txt"

positive_image_writer = open(positive_image_file, 'a')


#This script assumes it will be ran one directory
#above the positive images file. You can change
#the directory to adjust this
os.chdir(positive_images_direcotry)

for f in os.listdir("."):
    if re.match('.*\.jpg|.*\.png|.*\.bmp|.*\.gif|.*\.jpeg',f):
        positive_image_writer.write( os.getcwd() + "\\" + f + "\n" )
