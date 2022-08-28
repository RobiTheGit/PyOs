import webbrowser
import os
import sys
import subprocess
import colors
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
*[0] Terminal        *
*[1] Browser         *
*[2] Text Editor     *
*[3] Calculator      *
*[4] File Explorer   *
*[5] Calendar        *
*[6] Clock           *
*[7] Change Password *
**********************
Press Ctrl*Z to shutdown PyOs (not system)
'''
def main():
    subprocess.run('clear')
    print(pyoslogo.PyOsLoginLogo)
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
    time.sleep(2)
    subprocess.run('clear')
    apps()
    

def apps():
    numslists = ['0', '1', '2', '3', '4', '5', '6', '7']
    appslists = ['python3 term.py', 'webbrowser.open("https://www.google.com/")', 'vim', 'python3 calc.py', 'nautilus --new-window -s user/', 'python3 cal.py', 'python3 clock.py', 'python3 pswdset.py']
    print(f'\033{white}', appslist)
    print(f'Today is \033[1;36;40m {today}\033{c2}, Days til the new year, \033[1;33;40m', abs(timetilnyd.days), f'\033{c2}')
    print('Holdiays:',todayholiday)
    print('Welcome', f'\033{white}{username}')
    print('Message of the day:', messages.motd)
    app = input(f'\033[1;37;40mWhat app would you like to run? ')
    if app in numslists:
        x = numslists.index(app)
        y = appslists[x]
        if x != '1':
            try:
                subprocess.run('clear')
                subprocess.run(y, shell=True, check=True)
                recurse()
            except:
                   if app == '1':
                       webbrowser.open("https://www.google.com/")
                   else:
                       webbrowser.open("https://github.com/RobiTheGit/PyOs/issues") 
                   recurse()
        else:
            webbrowser.open("https://www.google.com/")
  
      
    else:
        print('INVALID APP!')
        time.sleep(1)
        subprocess.run('clear')
        recurse()
        
def recurse():
    subprocess.run('clear')
    apps()
    recurse()
    
subprocess.run('clear')
print('Starting ...')
time.sleep(0.5)        
main()
