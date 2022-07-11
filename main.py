import webbrowser
import os
import sys
import subprocess
import colors
import term
from datetime import date
today = date.today()
nyd = date(today.year, 12, 31)
timetilnyd = nyd - today

c1 = colors.ccodes[5]
c2 = colors.ccodes[0]

appslist = '''
[1] Terminal \n
[2] Browser \n
[3] Text Editor \n
[4] Calculator \n
[5] File Explorer\n
[6] Calendar\n
[7] Clock \n
[^Z] Shutdown PyOs (not system) \n
'''

def main():
    subprocess.run('clear')
    apps()

def apps():
    print(f"""\033{c1}
  ______   _____  ____  
 |  _ \ \ / / _ \/ ___| 
 | |_) \ V / | | \___ \ 
 |  __/ | || |_| |___) |
 |_|    |_| \___/|____/ 
                            
    \033{c2}""")
    print(f'Today is \033[1;36;40m {today}\033{c2}, Days til the new year, \033[1;33;40m', abs(timetilnyd.days), f'\033{c2}')
    print(appslist)
    app = input('What app would you like to run? ')
    if app == '1':
        term.init()
        subprocess.run('clear')
        recurse()
        
    elif app == '2':
        webbrowser.open_new('https://www.google.com/')
        subprocess.run('clear')
        recurse()
        
    elif app == '3':
        try:
            subprocess.run('vim')
        except FileNotFoundError:
            edit = input('techincal name for your text editor? ')
            subprocess.run(edit)    
        subprocess.run('clear')
        recurse()
        
    elif app == '4':
        subprocess.run('python3 calc.py', shell=True, check=True)
        subprocess.run('clear')
        recurse()
    elif app == '5':
        try:
            subprocess.run('nautilus --new-window -s PyOs', shell=True, check=True)
        except FileNotFoundError:
            browser = input('techincal name for your file browser? ')
            subprocess.run(browser)
            
        subprocess.run('clear')
        recurse()
        
    if app == '6':
        subprocess.run('python3 cal.py', shell=True, check=True)
        subprocess.run('clear')
        recurse() 
    
    if app == '7':
        term.exittype = 'main'
        subprocess.run('clear')
        term.clock()

      
    else:
        subprocess.run('clear')
        
def recurse():
    apps()
    recurse()
        
main()
