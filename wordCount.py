import sys
import re
import os
import subprocess

if len(sys.argv) is not 3:
    print("Correct usage: lab1.py <input text file> <output file>")
    exit()

#Assign variables to files
textFname = sys.argv[1]
outputFname = sys.argv[2]

# Make sure text file exists
if not os.path.exists(textFname):
    print ("text file input %s doesn't exist! Exiiting" % textFname)
    exit()

# Get input file open and ready to be read
tF = open (textFname, "r+")

# Get output file ready
oF = open(outputFname, "w+")

# create word dictionary and read and count all words
wordCount = {}
with open(textFname, "r") as textFile:
    for line in textFile:
        #Clean up words remove puntuation marks
        word_list = line.replace(',', ' ').replace(':', ' ').replace('.',' ').replace("'", ' ').replace("-", ' ').replace('"', ' ').lower().split()
        for word in word_list:
            if word not in wordCount:
                word = word.strip()
                wordCount[word] = 1
            else:
                wordCount[word] += 1
# Write words into output file
for item in sorted(wordCount.items()):
    oF.write("{} {}\n".format(*item))

oF.close()



