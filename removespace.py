import re #import the regular expressions module which allows escapes to use special characters using '\' like In The End could be In\ The\ End, like you would in a terminal
from pathlib import Path #from pathlib, import the paths so the program can read filepaths, and specificly paths since it says from pathlib import Path

regex = re.compile(r"[^a-zA-Z0-9.\-_]") # regex equals re finding a pattern with the files and searching for it

def rename(path): #define the function called rename with a variable called path
    name = re.sub(regex, "", path.name) # the file name equals 
    if name == path.name: #if the name is litterally the file path's name,
        return # return that info
    target = path.with_name(name) #target is equal to the file path, with the name, variable name
    if target.exists(): #if the target allready exists
        print(target, "exists. Failed to rename", name) #show the user that variable target(show it's name) exists, and it can't rename the old filename
        return #return this info
    path.rename(target) # rename the target file

def recurse(path, start=True): #new function recurse, using path, and now start is True
    for child in path.iterdir(): # for child paths, which are directories out of your home in the path when path points to a directory 
        if child.is_dir(): #if the child path is the directory
            recurse(child, False) #continue going, variables child and False
        else:  # files, etc.
            rename(child) # rename the child folder
    if not start: #if start not true
        rename(path) #rename the file path

start = input('WARNING! This will delete all spaces from this directory onwards, do you really want to do this? press ctrl-c to cancel, otherwise press enter')
recurse(Path()) #keep this going
