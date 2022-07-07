import webbrowser
import os
import sys
import subprocess
import colors
import term

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
[exit] exit \n'''

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
            subprocess.run('nautilus')
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
        term.clock()
               
    elif app == 'exit':
        term.exittype = 'term'
        term.exit()
        subprocess.run('clear')
        subprocess.run('pkill -9 -f main.py', shell=True, check=True)
        raise SystemExit
        subprocess.run('clear')
        subprocess.run('pkill -9 -f main.py', shell=True, check=True)
      
    else:
        subprocess.run('clear')
        
def recurse():
    apps()
    recurse()
        
main()
