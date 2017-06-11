#This program will take a text file resuts.txt and positive.txt (the names can be changed)
#and crop the images, once cropped, they will be resized to 50x50. This is
#neccessary since the hog feature extractors (OpenCV, and most others) require all images
#to be the same size. Any ratio and size can work but it needs to be consistent.

#You don't need to do anything for negative images except place the files in the folder
#negative_images

#Once the file is done running, check the folders named
#cropped_images under both positive_images and negative_images

#NOTE: This program assumes you are running it in the same directory as the positive.txt file

import os
import re
#It's probably overkill to use OpenCV for this script,
#but it's convenient.
import cv2

#You can customize these values for your specific situation
positive_images_file = "positive.txt"
positive_cropped_directory = "positive_images/cropped_images/"
negative_cropped_directory = "negative_images/cropped_images/"
negative_images_directory = "negative_images/" #where negative_images are stored
bounding_box_file = "results.txt"
width = 50
height = 50

#These variables are used to limit the number
#of negative images created from one sample.
#Without setting these, if you have a (WxH) 640X480 image.
#You will end up with 108 negative samples using the default 50x50 values.
#This is a lot of samples from one image, so these variables reduce those numbers
negative_column_buffer = 3
negative_row_buffer = 3
#End of general customization values


#This function crops all of the positive images
def crop_positive_images( ):

    positive_images_reader = open( positive_images_file, 'r' )

    bounding_box_reader = open( bounding_box_file, 'r' )

    positive_images = positive_images_reader.read( ).split("\n")

    #The format for the bounding boxes file is image_name, numOfBoxes, y, x, width, height
    #You can access the individual elements by .split(',') on each index
    #We can clean the trailing space that's in the data using this line of code
    #TODO: Fix this bug, don't just make a fix
    bounding_boxes = bounding_box_reader.read( )[0:len(bounding_box_reader.read())-1]

    bounding_boxes = bounding_boxes.split("\n")

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
            crop_img = cv2.resize(crop_img,(50, 50), interpolation = cv2.INTER_CUBIC)
            #This gives us the name of the image without the file path
            image_name = (single_bounding_box[ 0 ].split("\\"))[-1]

            cv2.imwrite( positive_cropped_directory + str(j) + "_" + image_name, crop_img )

#This function takes an image from the negative images directory and then cuts it
#into as many widthXheight pieces as it can
def crop_negative_images( ):

    for f in os.listdir(negative_images_directory):

        if re.match('.*\.jpg|.*\.png|.*\.bmp|.*\.gif|.*\.jpeg',f):

            crop_img = cv2.imread( negative_images_directory + f )

            #these variables hold the max num of cols and rows we can use
            #So a 200X200 image has a max of 2 50X50 cols and 2 50X50 rows.
            #the number of crops per image will of course depend on your widthXheight values
            tmp_height,tmp_width,channels = crop_img.shape
            max_cols = int(tmp_height / height)
            max_rows = int(tmp_width / width)

            for i in range(max_rows):
                for j in range(max_cols):
                    tmp_crop_img = crop_img[(j*height):((j*height)+height),(i*width):((i*width)+width)]
                    cv2.imwrite( negative_cropped_directory + str(i) + "_" + str(j) + "_" + f, tmp_crop_img )
            exit()

crop_positive_images( )
crop_negative_images( )
