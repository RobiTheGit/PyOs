import random
messagelist = ['print("The quick brown fox jumped over the lazy dog.")', 'if day == date.today(): \n    print("Hello")', 'python3 hello.py', 'subprocess.run("cat etc/motd", shell=True, check=True)', 'Monty Python is waiting for you', 'print("Hello World!")', 'https://www.python.org/', 'https://github.com/RobiTheGit/PyOs', 'Sorry Nothing', 'Error: No welcome message found!', 'There is no such thing as mistakes, just happy little accidents.']
x = random.randint(0, 10)
motd = messagelist[x]
