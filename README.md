# Pickled Forests

This RShiny app uses a python random forests implementation to achieve approximately 40% accuracy on the CIFAR-10 image data set.
The app makes predictions about images in real time using Python's pickle module.
The random forests implementation was "pickled", thus in order to call its "predict" method, 
all you have to do is reload the object from file. 

## Quick Start
  1. Clone this repo
  2. running install.sh should install all necessary Python dependencies.
  3. get the data set from https://www.kaggle.com/c/cifar-10/
  4. run mass_extract_pixels.py, making sure to appropriately change any file names to match the downloaded data set
    1. This takes the png files and creates a csv from the corresponding pixels
  5. running create_forest.py will train a forest based on the pixel data.
    1. It will also pickle both the forest and the pixel objects so that they can be easily retrieved in real time by the server.
  6. Start your RShiny App!

## Example App
https://freyja.cs.cofc.edu/spring2016_csci334user12/

You can tell that it makes real time predictions based on the load speed ;^)

![App Screenshot](/images/pickled-forests-screenshot.png?raw=true)
