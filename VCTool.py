from PIL import Image, ImageFilter
import cv2
import image_slicer
import os, pathlib
import numpy as np

GRID_SIZE = 625


def transformImage(directory):
	image = cv2.imread(directory)
	gsImage =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	(thresh, blackAndWhiteImage) = cv2.threshold(gsImage, 25, 255, cv2.THRESH_BINARY)
	#blackAndWhiteImage.save("blackAndWhiteImage.png")
	cv2.imwrite(IMAGE_DIRECTORY + "blackAndWhiteImage.png", blackAndWhiteImage)

def sliceImages(dir, imgDir, sliceDir):
	pathlib.Path(sliceDir).mkdir(parents = True, exist_ok=True)
	tiles = image_slicer.slice(IMAGE_DIRECTORY + "blackAndWhiteImage.png", 625, save=False)
	image_slicer.save_tiles(tiles, directory=IMAGE_DIRECTORY + "slices",\
	prefix='slice', format='png')

def binarize(image_to_transform):
	#image = cv2.imread(image_to_transform)
	pcounter = 0
	p = True
	image = Image.open(image_to_transform)
	w,h =image.size
	image = image.convert("RGB")
	for x in range(w):
		for y in range(h):
			r,g,b = image.getpixel((x,y))
			if(r!=00 or g != 00 or b!=00):
				pcounter = pcounter +1 
				#If pixel at specific spot is less then threshold add to count
	
	if(pcounter >= 50):
		p =False
	return p

def checkFiles(dir, count):
	for filename in os.listdir(dir):
		if(binarize(dir + filename) == False):
			count = count +1
			print(count)
	return count



count = 0
count = checkFiles("D:\Ayy lmao\Spring2021\HCI Project\Visual Complexity Pictures\Compass\Base Gauge\slices\\", count)
print("Total Grid Size: "+str(GRID_SIZE)+ " How Much Black Space: " + str(GRID_SIZE-count))

#Need to know Directory of Image, Image Name, grid size and percentage ratio
#Check to see if Directory ends with //


# transformImage(IMAGE_DIRECTORY + IMAGE_NAME)
# sliceImages(IMAGE_DIRECTORY, IMAGE_DIRECTORY + "blackAndWhiteImage.png", IMAGE_DIRECTORY + "\slices")


#sliceImages(IMAGE_DIRECTORY, IMAGE_DIRECTORY +)
# transformImage(IMAGE_DIRECTORY + IMAGE_NAME)
# pathlib.Path(IMAGE_DIRECTORY+"slices").mkdir(parents = True, exist_ok=True)

# tiles = image_slicer.slice(IMAGE_DIRECTORY + "blackAndWhiteImage.png", 625, save=False)
# image_slicer.save_tiles(tiles, directory=IMAGE_DIRECTORY + "slices",\
# prefix='slice', format='png')