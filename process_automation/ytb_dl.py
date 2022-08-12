#!/bin/python3

from pytube import YouTube
from sys import argv
from sys import stdout
from datetime import datetime as dt
import os
import time

class mycolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

line = "+" + 50 * '-' + "+"

# ----- BANNER ----- #
print(line)
print("  Youtube Downloader")
print("  Start Time : " + mycolors.OKGREEN + str(dt.now()) + mycolors.ENDC)
print(line)
print("\n")

# ----- Handle ARGV Errors ----- #
if not len(argv) == 2:
	print(mycolors.FAIL + "Error" + mycolors.ENDC + ": Use a YouTube link as arguments.")
	print("Only 1 arguments.\n")
	print(mycolors.OKBLUE + "Note" + mycolors.ENDC + ": If 'no matches found: <url>', try using double quotes.\n")
	exit()
url = argv[1]

# Output Video Statistics
print(mycolors.WARNING + "1." + mycolors.OKBLUE + "Getting Title and views ...\n" + mycolors.ENDC)

yt = YouTube(url)
print(mycolors.OKBLUE + "Title: " + mycolors.ENDC + f"{yt.title}")
print(mycolors.OKBLUE + "Views: " + mycolors.ENDC + f"{yt.views}\n")

# Download Video and Create Directory.
print(mycolors.WARNING + "2." + mycolors.OKBLUE + "Checking if directory to store the download exists ...\n" + mycolors.ENDC)
path = "./downloaded_video/"

if not os.path.exists(path):
	os.makedirs(path)

# ----- Start Download ----- #
print(mycolors.WARNING + "3." + mycolors.OKBLUE + "Start download...\n" + mycolors.ENDC)

yd = yt.streams.get_highest_resolution()
yd.download(path)

print(mycolors.OKBLUE + "Download Complete!" + mycolors.ENDC)




