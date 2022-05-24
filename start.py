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
