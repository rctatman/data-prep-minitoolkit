# modules we'll need
import glob
import os

# get input
addFilename = input("Do you want to add the name of the file to each line? (y/n)")
fileToCat = input("What files do you want to concatinate? (* will run over all files in the current directory, *.txt will run over all .txt files.)")
outputName = input("What do you want your output file to be called? (Include file extension.)")

# open a new file to save our output in
output = open(outputName,"w+")

# open every file in the current directory
for file in glob.glob(fileToCat):
    print(file)
    with open(file) as f:
        # read each line, add the name of the file to the start of 
        # it and then save it out
        for line in f.readlines():
            if addFilename == 'y':
                newline = os.path.splitext(file)[0] + "," + line
            else:
                newline = line
            output.write(line)
            
# close our file
output.close()