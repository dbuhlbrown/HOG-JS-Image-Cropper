# HOG-JS-Image-Cropper
A Javascript/Python script collection to assist with creating bounding boxes and cropping images for use with a SVM classifier using HOG features

<h3>Background and Usage</h3><br>

This project was designed to assist anyone doing machine learning using SVM with HOG features. I was not able to find any previous projects that
had the features I needed so I designed this collection of scripts. 

The basic requirements for HOG feature extraction is that all of the images need to be the same size. I chose 50x50 for my training since the object
I am trying to detect has a ratio of approximately 1:1. 

<h3>Application Pipeline</h3>

Begin by moving all positive and negative images you want to use into the "positive_images" and "negative_images" directories that you have defined in config.json.

<b>Step 1:</b>
Then run the "create_positives.py" script which will create a textfile named positive.txt which contains
a list of every image in the postive_images directory. 

<b>Step 2:</b>
Run the hog_cropper.html file. You will
then need to upload the positive.txt file to inform the Javascript of where each image you want to crop is located. 

Once this is done, press the button "Begin" and you can start drawing bounding boxes around the regions of interest (ROI). Press 'w' to 
write the current bounding box to the string which contains coordinates of the bounding boxes for the current image. 

Once you have selected all ROI press 's' to save the bounding boxes to the array which contains ALL bounding boxes.

If you are ready to take a break, or are done annotating images. Press "Save" and click the "Download" link
that is now visible. This will download a file called results.txt which contains all bounding boxes made. If you are done, go to step 4.

<b>Step 3: (If you want to save data and come back later)</b><br>
Since you may be annotating hundreds or thousands of images, it is crucial to be able to stop and come back to finish
at a later time. You can do this by pressing the "Save" button, once that is done. You will see a link that says "Download" you can
download the results for all images previously annotated. 

When you wish to continue annotating, begin at Step 1: but before you press "Begin" upload the "your_results_file.txt"
file to the input tag below the positive.txt once and simply press begin. You will then see that the program picks up where you left off. 

Continue annotating until all images are done.

<b>Step 4:</b>

Now that the annotation is done. You can run the "crop_images.py" file. This will crop the positive images (based on bounding boxes) to the proper width and height. 

<b>Note: The ratio in the cropper.js library and the ratio of width and height in the cropping library
need to be the same.</b><br>

Once it is finished running, you should have width/height selections from each negative image, and the ROI from your positive images.
These files will be saved in the "cropped_images" folders inside both the positive_images and negative_images folders.

Now you are ready to compute the HOG features and run a classifier on them.

<h3>Future Work and Extra Features</h3>

These items are in no particular order.

Edit the Javascript to read the proper ratio from the config.json file.

Rewrite the program to not use OpenCV (since it is a huge libary to import), but for now it is convenient to use it. 

Clean up and separate the Javascript code (it is inline currently). 

Improve the hog_cropper interface, it is pretty ugly right now.

Expand the Python unit testing (I only have basic testing currently)

<h3>Libraries / 3rd Party Software Used</h3>

For creating the bounding boxes I used cropper.js which can be found here: https://fengyuanchen.github.io/cropperjs/

I also use OpenCV (opencv.org) for reading and writing the images.
