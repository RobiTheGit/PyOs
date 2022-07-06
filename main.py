import webbrowser
import os
import sys
import subprocess
import colors
c1 = colors.ccodes[5]
c2 = colors.ccodes[0]
appslist = '''
[1] Terminal \n
[2] Browser \n
[3] Text Editor \n
[4] Calculator \n
[5] File Explorer\n
[e] exit \n'''

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
    print(appslist)
    app = input('What app would you like to run? ')
    if app == '1':
        subprocess.run('python3 term.py', shell=True, check=True)
        subprocess.run('clear')
        recurse()
        
    elif app == '2':
        print(webbrowser.get(using=None))
        webbrowser.open_new('https://www.google.com/')
        subprocess.run('clear')
        recurse()
        
    elif app == '3':
        subprocess.run('vim')
        subprocess.run('clear')
        recurse()
        
    elif app == '4':
        subprocess.run('python3 calc.py', shell=True, check=True)
        subprocess.run('clear')
        recurse()
    elif app == '5':
        try:
            subprocess.run('nautilus')
        except FileNotFoundError:
            browser = input('techincal name for your file browser? ')
            subprocess.run(browser)
            
        subprocess.run('clear')
        recurse()
        
    elif app == 'e':
        subprocess.run('clear')
        quit()
    else:
        subprocess.run('clear')
        
def recurse():
    apps()
    recurse()
            
main()
