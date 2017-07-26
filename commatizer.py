# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 09:59:55 2017

@author: rtatman
"""
import glob
import os

# get info from users
toReplace = input("What character do you want to replace with commas? (\\t = tab)")
whichFiles = input("Which files would you like to run this over? \n (* will run over all files in the current directory, *.txt will run over all .txt files.)")

# find all .txt files in the directory
files = glob.glob(whichFiles)

# read in file
for i in files:
    # create a new output file    
    outFile = os.path.splitext(i)[0] + ".csv"
    output = open(outFile, "w+")    
    
    # for lines in file, replace space with comma
    with open(i, "r") as input:
        for line in input:
            output.write(line.replace(toReplace, ","))

    
    # close output
    output.close() 
