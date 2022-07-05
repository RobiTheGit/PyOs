import os
import sys
from sys import argv
script, mode, name = argv

def mkdir():
    name = input('Directory name?')
    os.mkdir(name)
    
def rmdir():
    name = input('Directory name?')
    os.rmdir(name)

