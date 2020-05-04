#Image test
import os, sys
from PIL import Image
from PIL import ImageFilter
#Change directory of pictures to crop
path = "InputData/"
#How much to downscale by
directoryPath = path+ "Blurred"
#Allowed extensions
extensions = ['.jpg','.jpeg','.png']
#How intensely to blur
blurRadius = 2

#Create a new directory unless it already exists
try:
    os.mkdir(directoryPath)
    print("Directory ", directoryPath, " created.")
except FileExistsError:
    print("Directory ", directoryPath, " already exists.")

#Loop the input folder to find images
for infile in os.listdir(path):
    if infile.endswith(tuple(extensions)):
        print(infile)
        #Open the image
        i = Image.open(os.path.join(path, infile))
        print(i.format, i.size)
        #Apply Gaussian Blur to the image
        blurredImg = i.filter(ImageFilter.GaussianBlur(radius=blurRadius))
        #Split the file name and extension
        fn, fext = os.path.splitext(infile)

        #Save the new image in the cropped folder
        blurredImg.save('{}/Blurred/{}_blurred{}'.format(path, fn, fext))
