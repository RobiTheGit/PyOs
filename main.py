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
import messages

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
    todayholiday = "Dad's Birthday"
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
      
#*[x] App name*   
appslist = '''
**********************
*APPS MENU           *
*[1] Terminal        *
*[2] Browser         *
*[3] Text Editor     *
*[4] Calculator      *
*[5] File Explorer   *
*[6] Calendar        *
*[7] Clock           *
*[8] Change Password *
**********************
Press Ctrl*Z to shutdown PyOs (not system)
'''
def main():
    subprocess.run('clear')
    print(f'Login for {username}')
    passw = getpass.getpass('Password: ', stream=None)
    if passw == cpass:
        started()
    else:
        print('INVALID PASSWORD')
        time.sleep(0.5)
        main()
def started():
    subprocess.run('clear')
    print(f"""\033{c1}
    {PyOsLogo}                            
    \033{c2}""")
    print(f'Today is \033[1;36;40m {today}\033{c2}, Days til the new year, \033[1;33;40m', abs(timetilnyd.days), f'\033{c2}')
    print('Holdiays:',todayholiday)
    print('Welcome', f'\033{white}{username}')
    time.sleep(2)
    subprocess.run('clear')
    applistanimation()
    
def applistanimation():
    appslist = '''
**********************
*APPS MENU           *
********************** 
'''
    print(appslist)
    time.sleep(0.05)
    subprocess.run('clear')   
    appslist = '''
**********************
*APPS MENU           *
*[1] Terminal        *
********************** 
''' 
    print(appslist)
    time.sleep(0.05)
    subprocess.run('clear')   
    appslist = '''
**********************
*APPS MENU           *
*[1] Terminal        *
*[2] Browser         *
********************** 
''' 
    print(appslist)
    time.sleep(0.05)
    subprocess.run('clear')   
    appslist = '''
**********************
*APPS MENU           *
*[1] Terminal        *
*[2] Browser         *
*[3] Text Editor     *
********************** 
'''
    print(appslist)
    time.sleep(0.05)
    subprocess.run('clear')    
    appslist = '''
**********************
*APPS MENU           *
*[1] Terminal        *
*[2] Browser         *
*[3] Text Editor     *
*[4] Calculator      *
********************** 
''' 
    print(appslist)
    time.sleep(0.05)
    subprocess.run('clear')   
    appslist = '''
**********************
*APPS MENU           *
*[1] Terminal        *
*[2] Browser         *
*[3] Text Editor     *
*[4] Calculator      *
*[5] File Explorer   *
********************** 
''' 
    print(appslist)
    time.sleep(0.05)
    subprocess.run('clear')   
    appslist = '''
**********************
*APPS MENU           *
*[1] Terminal        *
*[2] Browser         *
*[3] Text Editor     *
*[4] Calculator      *
*[5] File Explorer   *
*[6] Calendar        *
********************** 
''' 
    print(appslist)
    time.sleep(0.05)
    subprocess.run('clear')   
    appslist = '''
**********************
*APPS MENU           *
*[1] Terminal        *
*[2] Browser         *
*[3] Text Editor     *
*[4] Calculator      *
*[5] File Explorer   *
*[6] Calendar        *
*[7] Clock           *
********************** 
''' 
    print(appslist)
    time.sleep(0.05)
    subprocess.run('clear')   
    appslist = '''
**********************
*APPS MENU           *
*[1] Terminal        *
*[2] Browser         *
*[3] Text Editor     *
*[4] Calculator      *
*[5] File Explorer   *
*[6] Calendar        *
*[7] Clock           *
*[8] Change Password *
********************** 
'''
    subprocess.run('clear') 
    apps()
    
          
def apps():
    print(appslist)
    print('Message of the day:', messages.motd)
    app = input(f'\033[1;37;40mWhat app would you like to run? ')
    
    if app == '1':
        term.init()
        subprocess.run('clear')
        recurse()
        
    elif app == '2':
        webbrowser.open*new('https://www.google.com/')
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
            subprocess.run('nautilus --new-window -s user/', shell=True, check=True)
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
    started()
    recurse()
    
subprocess.run('clear')
print('Starting ...')
time.sleep(0.5)        
main()
