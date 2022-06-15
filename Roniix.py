import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n     \x1b[1;97m\x1b[1;41m Powerd By Younis John\x1b[0m") 
    print("")
    print("\n\x1b[1;92m Congratulations Your Device Support This Tool\033[1;37m")
    print("\n\x1b[1;93m Please First Subscribe My YouTube Channel For Top Technology Tips & Tricks Thanku 🙂❤️\033[1;37m")
    os.system('xdg-open https://youtu.be/civNDQUwP2U/');time.sleep(6)
    import Ronixx
    Ronixx.Menu()
