import os
import time
import subprocess

def setpwd():
    f = open('user/password.pass', 'w')
    password = input('Set Password. ')
    f.write(password)

print('This should only be ran when your first get PyOs')
try:
    print('making directories')
    os.mkdir('user/Downloads')
    print('Downloads made')
    time.sleep(1)
    os.mkdir('user/Documents')
    print('Documents made')
    time.sleep(1)
    os.mkdir('user/Pictures')
    print('Pictures made')
    time.sleep(1)
    os.mkdir('user/Music')
    print('Music made')
    time.sleep(1)
    os.mkdir('user/Videos')
    print('Videos made')
    print('All Done with directories')
    setpwd()
except:
    setpwd()
