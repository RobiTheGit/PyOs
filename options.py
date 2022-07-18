import os
import getpass

def setpwd():
    f = open('user/password.pass', 'w')
    password = getpass.getpass('Password: ', stream=None)
    f.write(password)
    
    
    
def main():
    print('''
[1] Set Password \n  
    ''')
    option = input('What option would you like to set ') 
    if option == '1':
        setpwd()
main()
