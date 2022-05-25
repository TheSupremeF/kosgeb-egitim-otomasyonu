import os
import sys
import time
from scripts.kosgeb import *

from zoneinfo import available_timezones

# test json import

print(' _  ______   _____  _____ ______ ____  ')
print(' | |/ / __ \ / ____|/ ____|  ____|  _ \ ')
print(' | . / |  | | (___ | |  __| |__  | |_) |')
print(' |  <| |  | |\___ \| | |_ |  __| |  _ < ')
print(' | . \ |__| |____) | |__| | |____| |_) |')
print(' |_|\_\____/|_____/ \_____|______|____/ ')
print('           EĞİTİM OTOMASYONU            ')
time.sleep(1)
print('----------------------------------')
print('v2.1')
print('----------------------------------')
print('developed by:')
time.sleep(0.5)
print('Kuray Karaaslan')
time.sleep(0.5)
print('Mustafa Burak Besler')
time.sleep(0.2)
print('.')
time.sleep(0.2)
print('..')
time.sleep(0.2)
print('...')
time.sleep(0.2)

# This is checking if the user is using a Linux, Windows, or Mac OS.
if sys.platform == 'linux':
    # check chrome is installed
    if not os.path.isfile('/usr/bin/google-chrome'):
        os.system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
        #install deb
        os.system('sudo dpkg -i google-chrome-stable_current_amd64.deb')
        #remove deb
        os.system('rm google-chrome-stable_current_amd64.deb')
        #print success
        print('chrome installed')

    #check for chrome version
    chrome_version = os.popen('google-chrome --version').read()

    #check webdriver is installed
    if not os.path.isfile('/usr/bin/chromedriver'):
        #warn user to install and exit
        print('chromedriver is not installed')
        print('please install chromedriver and try again')
        sys.exit()

    #check for webdriver version
    webdriver_version = os.popen('chromedriver --version').read()

    #check webdriver version is compatible with chrome version
    if not chrome_version[0:5] == webdriver_version[0:5]:
        #warn user to install compatible version and exit
        print('chromedriver is not compatible with chrome version')
        print('please install chromedriver version compatible with chrome version')
        sys.exit()
elif sys.platform == 'win32':
    #check chrome is installed
    if not os.path.isfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'):
        print('chrome is not installed')
        print('please install chrome and try again')
        sys.exit()

    #check for chrome version
    chrome_version = os.popen('chrome --version').read()

    #check webdriver is installed
    if not os.path.isfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'):
        #warn user to install and exit
        print('chromedriver is not installed')
        print('please install chromedriver and try again')
        sys.exit()

    #check for webdriver version
    webdriver_version = os.popen('chromedriver --version').read()

    #check webdriver version is compatible with chrome version
    if not chrome_version[0:5] == webdriver_version[0:5]:
        #warn user to install compatible version and exit
        print('chromedriver is not compatible with chrome version')
        print('please install chromedriver version compatible with chrome version')
        sys.exit()
elif sys.platform == 'darwin':
    #check chrome is installed
    if not os.path.isfile('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'):
        print('chrome is not installed')
        print('please install chrome and try again')
        sys.exit()

    #check for chrome version
    chrome_version = os.popen('google-chrome --version').read()

    #check webdriver is installed
    if not os.path.isfile('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'):
        #warn user to install and exit
        print('chromedriver is not installed')
        print('please install chromedriver and try again')
        sys.exit()

    #check for webdriver version
    webdriver_version = os.popen('chromedriver --version').read()

    #check webdriver version is compatible with chrome version
    if not chrome_version[0:5] == webdriver_version[0:5]:
        #warn user to install compatible version and exit
        print('chromedriver is not compatible with chrome version')
        print('please install chromedriver version compatible with chrome version')
        sys.exit()
else:
    print('this OS is not supported')
    sys.exit()

# Checking if the selenium module is installed. If it is not installed, it will print the message and
# exit the program.
try:
    import selenium
except ImportError:
    print('selenium module is not installed')
    print('please install selenium module and try again')
    sys.exit()

while True:
        print('T.C. Kimlik Numaranızı giriniz:')
        tc_kimlik_no = input()
        if len(tc_kimlik_no) != 11:
            print('T.C. Kimlik numaranız 11 haneden kısa veya uzun olmamalıdır')

        print('E-Devlet Şifrenizi giriniz')
        e_devlet_sifreniz = input()
        print('----------------------------------')
        print('\n')
        print('available choices:')
        print('[1] - Geleneksel Girişimci Eğitimi')
        print('[2] - İleri Girişimcilik Eğitimi')
        print('[3] - Eğitim Kodu Gireceğim')
        print('[4] - Exit')

        while True:
            choice = input('\n\nSeçim: ')
            if choice == '1':
                kosgeb(tc_kimlik_no, e_devlet_sifreniz, 1)
            elif choice == '2':
                kosgeb(tc_kimlik_no, e_devlet_sifreniz, 2)
            elif choice == '3':
                target = input('\n\nEğitim kodunu giriniz: ')
                kosgeb(tc_kimlik_no, e_devlet_sifreniz, target)
            elif choice == '4':
                sys.exit()
            else: False 
            print('Hatalı giriş')
