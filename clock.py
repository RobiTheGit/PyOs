def clock():
    print('PyOs Clock')
    try:
        print(time.ctime())
        time.sleep(1)
        subprocess.run('clear')
        clock()
    except:
       subprocess.run('python3 main.py', shell=True, check=True)

clock()
