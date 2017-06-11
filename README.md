# HOG-JS-Image-Cropper
A Javascript/Python script collection to assist with creating bounding boxes and cropping images for use with a SVM classifier using HOG features

<b>Background and Usage</b><br>

This project was designed to assist anyone doing machine learning using SVM with HOG features. I was not able to find any previous projects that
had the features I needed so I designed this collection of scripts. 

The basic requirements for HOG feature extraction is that all of the images need to be the same size. I chose 50x50 for my training since the object
I am trying to detect has a ratio of approximately 1:1. 

<b>Application Pipeline</b>

Begin by moving all positive and negative images you want to use into the "positive_images" and "negative_images" directories.

<i>Step 1:</i>
Then run the "create_positives.py" script which will create a textfile named positive.txt which contains
a list of every image in the postive_images directory. 

<i>Step 2:</i>
Run the hog_cropper.html file. You will
then need to upload the positive.txt file to inform the Javascript of where each image you want to crop is located. 

Once this is done, press the button "Begin" and you can start drawing bounding boxes around the regions of interest (ROI). Press 'w' to 
write the current bounding box to the string which contains coordinates of the bounding boxes for the current image. 

Once you have selected all ROI press 's' to save the bounding boxes to the array which contains ALL bounding boxes.

If you are ready to take a break, or are done annotating images. Press "Save" and click the "Download" link
that is now visible. This will download a file called results.txt which contains all bounding boxes made. If you are done, go to step 4.

<i>Step 3: (If you want to save data and come back later)</i><br>
Since you may be annotating hundreds or thousands of images, it is crucial to be able to stop and come back to finish
at a later time. You can do this by pressing the "Save" button, once that is done. You will see a link that says "Download" you can
download the results for all images previously annotated. 

When you wish to continue annotating, begin at Step 1: but <b>before<b> you press "Begin" upload the "[your_results_file].txt"
file to the input tag below the positive.txt once and simply press begin. You will then see that the program picks up where you left off. 

Continue annotating until all images are done.

<i>Step 4:</i>



<b>Future Work and Extra Features</b>

<b>Libraries / 3rd Party Software Used</b>

For creating the bounding boxes I used cropper.js which can be found here: https://fengyuanchen.github.io/cropperjs/

I also use OpenCV (opencv.org) for reading and writing the images.
