#!/bin/python3

from PIL import Image, ImageEnhance, ImageFilter
import os
from datetime import datetime as dt

class mycolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

line = "+" + 50 * '-' + "+"
path = './pics/img'
pathOut = './pics/editedImg'
i = 1

# BANNER
print(line)
print("  Image Editor : rotate + B&W + Enhance contrast")
print("  Scanning targets : " + mycolors.WARNING + f"{path}" + mycolors.ENDC)
print("  Start Time : " + mycolors.OKGREEN + str(dt.now()) + mycolors.ENDC)
print(line)
print("\n")


for filename in os.listdir(path):
	# Open the image located in ./path/file
	print(mycolors.OKGREEN + f"Opening Img {i}..." + mycolors.ENDC)
	img = Image.open(f"{path}/{filename}")

	# Edit the image
	# .convert('L') to black&white the image
	# .rotate(-90) to rotate the img
	print(f"Apply modifications to Img {i}...")
	edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

	# Increase contrast
	factor = 1.25
	enhancer = ImageEnhance.Contrast(edit)

	edit = enhancer.enhance(factor)

	# Clean the name
	clean_name = os.path.splitext(filename)[0]

	# Save
	print(f"Save Img {i}...\n/\n")
	edit.save(f'{pathOut}/{clean_name}_edited.jpeg')

	i += 1
