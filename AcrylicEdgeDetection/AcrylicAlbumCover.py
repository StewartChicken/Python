#Imports
import PIL
import os
from PIL import Image, ImageFilter, ImageChops, ImageEnhance

#Desired pixel size of the output images (500 x 500)
desired_size = 500

#Input/output paths
path = r"[INSERT PATH]"
save_path = r"[INSERT OUTPUT PATH]"	

#Renames all the files in the directory to incrementing numbers

'''index = 0
for file in os.listdir(path):
	img_path = f"{path}//{file}"
	img_rename = f"{path}//{index}.png"
	os.rename(img_path, img_rename)
	index += 1'''

#Crops each 800 x 1000 spotify image (cuts out spotify's song code) and resizes it to 
#the desired pixel width/height. Takes each image and converts it to black/white, finds the edges,
#inverts it, and boosts the contrast for laser cutting. 
for file in os.listdir(path):
	
	img_path = f"{path}//{file}"
	img = Image.open(img_path)

	w, h = img.size

	img = img.crop((0, 0, w, 800))
	img = img.resize((desired_size, desired_size)) #Resizes
		
	img = img.convert("L") #Grayscale
	img = img.filter(ImageFilter.FIND_EDGES) #Edge detection
	img = ImageChops.invert(img) #Inverts image

	contrast_booster = ImageEnhance.Contrast(img) #Boosts image contrast 
	img = contrast_booster.enhance(2)

	img.save(rf"OUTPUT PATH{file}") #Saves final images
