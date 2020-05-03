#Image test
import os, sys
from PIL import Image
count = 1
failCount = 0
#Path to the data folder
path = "InputData/"
directoryPath = path+ "Cropped"
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
        i = Image.open(os.path.join(path, infile))
        print(i.format, i.size)
        #Don't crop if height is < 300px
        if i.height < 300:
            box = box = (0, 0, i.width, i.height)
        #Else crop height to save top 300px
        else:
            box = (0, 0, i.width, 300)
        #Select the region that is to be saved
        region = i.crop(box)
        #Split the file name and extension
        fn, fext = os.path.splitext(infile)

        #Save the selected region
        region.save('{}/Cropped/{}_Cropped{}'.format(path, fn, fext))

        count += 1
    else:
        failCount += 1
if count > 1:
    print("Cropped "+ str(count - 1) + " images to the " + path + " directory.")
else:
    print("No images were cropped.")
if failCount > 1:
    print("Failed to crop "+ str(failCount) + " files.")