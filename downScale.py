#Image test
import os, sys
from PIL import Image
#Change directory of pictures to crop
path = "InputData/"
#How much to downscale by
divideBy = 5
directoryPath = path+ "Downscaled"
#Allowed extensions
extensions = ['.jpg','.jpeg','.png']

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
        #Divide height and width based on given number
        newHeight = round(i.height / divideBy)
        newWidth = round(i.width / divideBy)
        #Resize the image to its new size
        i = i.resize((newWidth, newHeight),Image.ANTIALIAS)
        #Split the file name and extension
        fn, fext = os.path.splitext(infile)

        #Save the new image in the cropped folder
        i.save('{}/Downscaled/{}_downscaled{}'.format(path, fn, fext))
