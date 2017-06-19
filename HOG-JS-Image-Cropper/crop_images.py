#This program will take a text file resuts.txt and positive.txt (the names can be changed)
#and crop the images, once cropped, they will be resized to widthxheight. This is
#neccessary since the hog feature extractors (OpenCV, and most others) require all images
#to be the same size. Any ratio and size can work but it needs to be consistent.

#You don't need to do anything for negative images except place the files in the folder
#negative_images

#Once the file is done running, check the folders named
#cropped_images under both positive_images and negative_images

import os
import re
import json
#It's probably overkill to use OpenCV for this script,
#but it's convenient.
import cv2

class ImageCropper:

#These variables are used to limit the number
#of negative images created from one sample.
#Without setting these, if you have a (WxH) 640X480 image.
#You will end up with 108 negative samples using the default 50x50 values.
#This is a lot of samples from one image, so these variables reduce those numbers
#negative_column_buffer = 7
#negative_row_buffer = 7


#End of general customization values

    def __init__(self):

        #These variables can be customized inside config.json
        self.positive_images_file = ""
        self.positive_cropped_directory = ""
        self.negative_cropped_directory = ""
        self.negative_images_directory = ""
        self.bounding_box_file = ""

        self.width = 0
        self.height = 0
        self.negative_row_buffer = -1
        self.negative_column_buffer = -1

    #Reads the config.json file to set up the general variables
    def read_config_file(self, config_file_name):

        config_data_file = open(config_file_name,"r")

        config_data = json.loads(config_data_file.read())

        self.positive_images_file = config_data["positive_images_file"]
        self.positive_cropped_directory = config_data["positive_cropped_directory"]

        self.negative_cropped_directory = config_data["negative_cropped_directory"]
        self.negative_images_directory = config_data["negative_images_directory"]

        self.bounding_box_file = config_data["bounding_box_file"]

        self.width = config_data["width"]
        self.height = config_data["height"]
        self.negative_row_buffer = config_data["negative_column_buffer"]
        self.negative_column_buffer = config_data["negative_column_buffer"]

    #This function takes the bounding_box data and cleans it up
    #I.E. removing --SKIPPED-- and the last empty line.
    def extract_bounding_boxes(self):

        bounding_box_reader = open( self.bounding_box_file, 'r' )

        bounding_boxes = bounding_box_reader.read( )[0:len(bounding_box_reader.read())-1]

        bounding_boxes = bounding_boxes.split("\n")

        #I added this to simplify the operation of skipping --SKIPPED-- lines
        bounding_boxes = list( filter(("--SKIPPED--").__ne__,bounding_boxes))

        return bounding_boxes

    #This function crops all of the positive images
    def crop_positive_images(self):

        #The format for the bounding boxes file is image_name, numOfBoxes, y, x, width, height
        #You can access the individual elements by .split(',') on each index
        #We can clean the trailing space that's in the data using this line of code
        #TODO: Fix this bug, don't just make a fix

        bounding_boxes = self.extract_bounding_boxes( )

        for i in range ( len(bounding_boxes) ):

            single_bounding_box = bounding_boxes[ i ].split(",")

            image = cv2.imread( single_bounding_box[0] );

            #This loop is a bit complicated because of the format our data is
            #But have a simple data file is worth one complicated loop
            for j in range( 0, int(single_bounding_box[1])*4, 4 ):

                y = int( single_bounding_box[j+2] )
                x = int( single_bounding_box[(j+1)+2] )
                width = int( single_bounding_box[(j+2)+2] )
                height = int( single_bounding_box[(j+3)+2] )
                #Debugging print left in for test
                #print (   single_bounding_box[j+2] + ","
                #        + single_bounding_box[(j+1)+2] + ","
                #        + single_bounding_box[(j+2)+2] + ","
                #        + single_bounding_box[(j+3)+2]
                #      )

                crop_img = image[y:(y+height),x:(x+width)]
                crop_img = cv2.resize(crop_img,(self.width, self.height), interpolation = cv2.INTER_CUBIC)
                #This gives us the name of the image without the file path
                image_name = (single_bounding_box[ 0 ].split("\\"))[-1]

                cv2.imwrite( self.positive_cropped_directory + str(j) + "_" + image_name, crop_img )


    #This function determines the buffers around the negative images
    def compute_negative_buffers(self,max_cols,max_rows):

        #We are assuming the main info of the image is
        #in the center, so we create a buffer of X,Y so that
        #we won't end up with tons of negative samples of nothing
        if max_cols < self.negative_column_buffer or max_cols == self.negative_column_buffer:
            negative_column_buffer = 0
        else:
            negative_column_buffer = self.negative_column_buffer

        if max_rows < self.negative_row_buffer or max_rows == self.negative_row_buffer:
            negative_row_buffer = 0
        else:
            negative_row_buffer = self.negative_row_buffer

        return negative_column_buffer, negative_row_buffer

    #This function takes an image from the negative images directory and then cuts it
    #into as many widthXheight pieces as it can
    def crop_negative_images(self):

        for f in os.listdir(self.negative_images_directory):

            if re.match('.*\.jpg|.*\.png|.*\.bmp|.*\.gif|.*\.jpeg',f):

                crop_img = cv2.imread( self.negative_images_directory + f )

                #these variables hold the max num of cols and rows we can use
                #So a 200X200 image has a max of 2 50X50 cols and 2 50X50 rows.
                #the number of crops per image will of course depend on your widthXheight values
                tmp_height,tmp_width,channels = crop_img.shape
                max_cols = int(tmp_height / self.height)
                max_rows = int(tmp_width / self.width)

                negative_column_buffer,negative_row_buffer = self.compute_negative_buffers( max_cols,max_rows)

                for i in range(negative_row_buffer,max_rows,1):
                    for j in range(negative_column_buffer,max_cols,1):
                        tmp_crop_img = crop_img[(j*self.height):((j*self.height)+self.height),(i*self.width):((i*self.width)+self.width)]
                        cv2.imwrite( self.negative_cropped_directory + str(i) + "_" + str(j) + "_" + f, tmp_crop_img )

imageCropper = ImageCropper( )
imageCropper.read_config_file("config.json")
imageCropper.crop_positive_images()
imageCropper.crop_negative_images()
