# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 09:59:55 2017

@author: rtatman
"""
import glob
import os

whichFiles = input("Which files would you like to remove commas from? (* will run over all files in the current directory, *.txt will run over all .txt files.)")

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
            output.write(line.replace(",", ""))

    
    # close output
    output.close() 
