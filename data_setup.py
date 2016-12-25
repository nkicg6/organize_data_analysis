#python3
""" Set up a data analysis project by creating a home directory and adding
necessary files and directories.Will create new directories in the current
working directory. Will also git init the main directory.Organization based on:
https://www.youtube.com/watch?v=JI1HWUAyJHE&t=169s&index=238&list=WL
Key:
    [ISO_date]-[author_initials]-[2-4 word description].ipynb
author: Nick George"""


import sys
import os
main_directory = sys.argv[1]
if os.path.exists(main_directory):
    print("A directory named" + sys.arg[1] + " already exists in this working directory.")
    sys.exit("Error: Directory already exitst." )
else:
    new_main_directory = os.path.join(os.getcwd(), main_directory)
    os.mkdir(new_main_directory)

def make_subdirs(subname):
    print("making directory: ", subname)
    os.chdir(new_main_directory)
    os.mkdir(os.path.join(new_main_directory, subname)

make_subdirs("Deliver")
make_subdirs("Develop")
make_subdirs("Figures")
make_subdirs("scripts")
make_subdirs("Data")

def readme_files(filename,text):
    print("creating file ", filename)
    os.chdir(new_main_directory)
    file_ = open(filename, 'w')
    file_.write(text)
    file_.close()

#write readmes
readme_files(".gitignore", "/Data")
readme_files("readme.md","[ISO_date]-[author_initials]-[2-4 word description].ipynb /n author: Nick George")
#TODO  git init
# possibly from a shell script?
sys.exit("Done")

