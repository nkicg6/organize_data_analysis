#python3
""" Set up a data analysis project by creating a home directory and adding
necessary files and directories.Will create new directories in the home directory.
Will also git init the main directory.Organization based on:
https://www.youtube.com/watch?v=JI1HWUAyJHE&t=169s&index=238&list=WL
Key for for .ipynb files that will be saved in these directories:
    [ISO_date]-[author_initials]-[2-4 word description].ipynb

author: Nick George"""


import sys
import os
#change to home directory crossplatform

os.chdir(os.path.expanduser("~"))

main_directory = os.path.join(os.getcwd(),sys.argv[1])

if os.path.exists(main_directory):
    print("A directory named" + sys.argv[1] + " already exists in your home directory.")
    sys.exit("Error: Directory already exists." )
else:
    print("Setting up project in: " + sys.argv[1])
    print("Filepath: " + main_directory)
    os.mkdir(main_directory)

def make_subdirs(subname):
    print("making directory: ", subname)
    os.chdir(main_directory)
    os.mkdir(os.path.join(main_directory, subname))

make_subdirs("Deliver")
make_subdirs("Develop")
make_subdirs("Figures")
make_subdirs("scripts")
make_subdirs("Data")

def readme_files(filename,*args):
    print("creating file ", filename)
    os.chdir(main_directory)
    file_ = open(filename, 'w')
    for line in args:
        file_.write(line+'\n')
    file_.close()

#write readmes
readme_files(".gitignore", "/Data")
readme_files("readme.md","ipynb naming Key: [ISO_date]-[author_initials]-[2-4 word description].ipynb", "author: Nick George","MORE PROJECT INFO HERE")
#TODO  git init
#TODO add datestamp to readme.md file. Optional argument in readme function.
# https://gist.github.com/nathania/2840185
# possibly from a shell script?
sys.exit("Done")

