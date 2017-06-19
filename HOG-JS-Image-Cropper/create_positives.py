#This file just creates a positive.txt text file which contains the image names (with full paths)
#That can be used with the hog_cropper file
#If you need to change the file paths, edit the config.json file
import os
import re
import json

config_data_file = open("config.json","r")
config_data = json.loads(config_data_file.read())

positive_images_file = config_data["positive_images_file"]
positive_images_directory = config_data["positive_images_directory"]
positive_image_writer = open(positive_images_file, 'w+')

#This script assumes it will be ran one directory
#above the positive images file. You can change
#the directory to adjust this
owd = os.getcwd()
os.chdir(positive_images_directory)

positive_image_list  = os.listdir(".")

cwd = os.getcwd()
os.chdir(owd)

for f in positive_image_list:
    if re.match('.*\.jpg|.*\.png|.*\.bmp|.*\.gif|.*\.jpeg',f):
        positive_image_writer.write( cwd + "\\" + f + "\n" )
