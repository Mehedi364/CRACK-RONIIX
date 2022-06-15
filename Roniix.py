import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations Your Device Support This Tool\033[1;37m")
    print("\n\x1b[1;93m First Subscribe My YouTube Channel\033[1;37m")
    os.system('xdg-open https://youtu.be/civNDQUwP2U/');time.sleep(3)
    import Ronixx
    Ronixx.Menu()
