import os
import subprocess
import sys
import time
import colors
import mkfil

home = os.getcwd()
dire = ''
exittype = 'term'
c1 = colors.ccodes[5]
c2 = colors.ccodes[0]
c3 = colors.ccodes[1]
prevdire = ''
def exit():
    try:
        if exittype == 'term':
             raise SystemExit
        else:
            subprocess.run('python3 main.py', shell=True, check=True)
    except:
         subprocess.run('python3 main.py', shell=True, check=True)
         subprocess.run('pkill -9 -f term.py', shell=True, check=True)
         sys.exit(0)
         exit()
         quit()
def cd():
    global dire
    global prevdire
    dire = input('Which directory to cd into? ')
    if dire == '' or dire == 'Home' or dire.startswith('/') or dire.startswith('C:'):
        if dire.startswith('/media'):
            os.chdir(dire)
        else:
            os.chdir(home)
            dire = ''
    else:
        try:
             os.chdir(dire)
        except:
            print('No Such Directory')
            dire = prevdire
            
def spaceremoval():
    subprocess.run('python3 removespace.py', shell=True, check=True)
    recurse()
def clock():
    print('PyOs Clock')
    try:
        print(time.ctime())
        time.sleep(1)
        subprocess.run('clear')
        clock()
    except:
        if exittype == 'term':
             recurse()
        else:
            subprocess.run('python3 main.py', shell=True, check=True)
def colorset():
    global c1
    global c2
    global c3
    print(colors.cnames)
    x = input('Choose Number from color list for color 1 ')
    x = int(x)
    c1 = colors.ccodes[x]
    x = input('Choose Number from color list for color 2 ')
    x = int(x)
    c2 = colors.ccodes[x]
    x = input('Choose Number from color list for color 3 ')
    x = int(x)
    c3 = colors.ccodes[x]
    recurse()
    
def loop():
    global dire
    global prevdire
    global c1
    global c2
    global c3
    prevdire = dire
    command = input(f'\033{c1}User@Pyterm\033{c2}:\033{c3}~/{dire}\033[1;37;40m$ ')
    if command == 'exit': 
        exit()
        
    if command == 'ctime':
        clock()

    if command == 'gui':
        subprocess.run('python3 main.py', shell=True)
        
        
    if command == 'colorset':
        colorset()
    
    if command == 'rmspaces':
        spaceremoval()
        
    if command == 'disptest':
        print(colors.disptest)
        recurse()
    
    if command == 'mkfil' or command.startswith('touch'):
       mkfil.mkfil()
       recurse()
    
    if command == 'rmfil' or command.startswith('rm'):
        mkfil.delfil()
        recurse()  
    
    try:
        subprocess.run(command, shell=True, check=True)
        if command.startswith('cd ') or command == 'cd': #i didn't sparate this one so showing the current directory would work
            cd()
    except:
        if command == 'ctime'or command == 'disptest' or command == 'colorset':
            recurse()
        else:
            print('\033[1;31;40m Error \033[1;37;40m')
            recurse()
    

    recurse()
    

def recurse():    
    try:
        loop()
        recurse()
    except:
        subprocess.run('python3','main.py')


def init():
    subprocess.run('clear')
    recurse()



