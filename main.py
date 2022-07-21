import webbrowser
import os
import sys
import subprocess
import colors
import term
import time
import getpass
from datetime import date
import pyoslogo

correctpass = open('user/password.pass')
cpass = correctpass.read()
today = date.today()
nyd = date(today.year, 12, 31)
timetilnyd = nyd - today
white = colors.ccodes[0]
PyOsLogo = pyoslogo.PyOsLogo
theme = ''
username = getpass.getuser()

if today == date(today.year, 12, 25):
    todayholiday = 'Christmas'
    PyOsLogo =pyoslogo.PyOSLogoC
    theme = 'Festive'
    
elif today == date(today.year, 12, 24):
    todayholiday = 'Christmas Eve'
    PyOsLogo =pyoslogo.PyOSLogoC
    theme = 'Festive'
    
elif today == date(today.year , 1, 1 ):
    todayholiday = 'New Years Day'
    PyOsLogo = pyoslogo.PyOsLogoA
    theme = 'America'
    
elif today == nyd:
    todayholiday = 'New Years Eve'
    theme = 'America'
    PyOsLogo = pyoslogo.PyOsLogoA
    
elif today == date(today.year, 7, 4):
    todayholiday = 'Fourth of July'
    theme = 'America'
    c1 = colors.ccodes[6]
    c2 = colors.ccodes[3]
    PyOsLogo = pyoslogo.PyOsLogoA
    
elif today == date(today.year, 10, 31):
    todayholiday = 'Halloween'
    theme = 'Spooky'
    PyOsLogo = pyoslogo.PyOSLogoH
    
elif today == date(today.year, 9, 28):
    todayholiday = 'Dad\'s Birthday'
    PyOsLogo =pyoslogo.PyOSLogo
    theme = 'Spooky'
else:
    todayholiday = ''   
   
if theme == 'Festive':
    c1 = colors.ccodes[5]
    c2 = colors.ccodes[6]

elif theme == 'Spooky':
    c1 = colors.ccodes[4]
    c2 = colors.ccodes[4] 
elif theme == 'America':
    c1 = colors.ccodes[6]
    c2 = colors.ccodes[3]
else:
    c1 = colors.ccodes[5]
    c2 = colors.ccodes[1] 
      
#[x] App name    
appslist = '''
[1] Terminal \n
[2] Browser \n
[3] Text Editor \n
[4] Calculator \n
[5] File Explorer\n
[6] Calendar\n
[7] Clock \n
[8] Change Password \n
Press Ctrl_Z to shutdown PyOs (not system) \n
'''
def main():
    subprocess.run('clear')
    print(f'Login for {username}')
    passw = getpass.getpass('Password: ', stream=None)
    if passw == cpass:
        apps()
    else:
        print('INVALID PASSWORD')
        time.sleep(0.5)
        main()
        
def apps():
    subprocess.run('clear')
    print(f"""\033{c1}
    {PyOsLogo}                            
    \033{c2}""")
    print(f'Today is \033[1;36;40m {today}\033{c2}, Days til the new year, \033[1;33;40m', abs(timetilnyd.days), f'\033{c2}')
    print('Holdiays:',todayholiday)
    print('Welcome', f'\033{white}{username}')
    print(appslist)
    app = input(f'\033[1;37;40mWhat app would you like to run? ')
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
            subprocess.run('nautilus --new-window -s user', shell=True, check=True)
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
        
    if app == '8':
        subprocess.run('python3 options.py', shell=True, check=True)
        subprocess.run('clear')
        recurse()
      
    else:
        print('INVALID APP!')
        time.sleep(1)
        subprocess.run('clear')
        recurse()
        
def recurse():
    apps()
    recurse()
        
main()
