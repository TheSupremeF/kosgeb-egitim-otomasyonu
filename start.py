import os
import sys
import time
from scripts.kosgeb import *
from logindata import *

from zoneinfo import available_timezones

# test json import

print('\n')
print('Kosgeb eğitim otomasyonu')
print('----------------------------------')
print('version 1.0')
print('----------------------------------')
print('developed by: Kuray Karaaslan')

print('----------------------------------')
print('\n')
print('available chooices:')
print('[1] - Geleneksel Girişimci Eğitimi')
print('[2] - İleri Girişimcilik Eğitimi')
print('[3] - Eğitim Kodu Gireceğim')
print('[3] - Exit')

while True:
    choice = input('\n\nchoice: ')
    if choice == '1':
        kosgeb(tc_kimlik_no, e_devlet_sifreniz, 1)
    elif choice == '2':
        kosgeb(tc_kimlik_no, e_devlet_sifreniz, 2)
    elif choice == '3':
        target = input('\n\nEğitim kodunu giriniz: ')
        kosgeb(tc_kimlik_no, e_devlet_sifreniz, target)
    elif choice == '4':
        sys.exit()
