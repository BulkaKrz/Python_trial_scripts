# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:04:29 2023
Create 
Based on:
Vaughan, Lee. Python mniej poważnie. Red. . Warszawa: Wydawnictwo Naukowe PWN, 2020, 453 s. ISBN 978-83-01-20998-8
Chapter 1

Names in Poland
https://dane.gov.pl/pl/dataset/219,imiona-nadawane-dzieciom-w-polsce
Surnames
https://dane.gov.pl/pl/dataset/568/resource/36405,nazwiska-meskie-stan-na-2022-01-27/table?page=1&per_page=20&q=&sort=

"""

import sys, random
import pandas as pd

print("Welcome to the names generator'\n")


surname = pd.read_csv(r'D:\REPOZYTORY\Python_trial_scripts\NAZWISKA_MĘSKIE-Z_UWZGLĘDNIENIEM_OSÓB_ZMARŁYCH.csv', 
                         usecols=['Nazwisko aktualne'])

surname = surname['Nazwisko aktualne']
last = tuple(surname.values.tolist())
last

name = pd.read_csv(r'D:\REPOZYTORY\Python_trial_scripts\4-_WYKAZ_IMION_MĘSKICH_NADANYCH_DZIECIOM_URODZONYM_W_2022_R._WG_POLA_IMIĘ_PIERWSZE__STATYSTYKA_SZCZEGÓŁOWA_WG_WOJ._REJESTRACJI_URODZENIA.csv', 
                         usecols=['IMIĘ PIERWSZE'])

name = name['IMIĘ PIERWSZE']
first = tuple(name.values.tolist())
first

     

while True:

    firstName = random.choice(first)

    lastName = random.choice(last)

  
    print('\n', '-'*50,'\n' ,firstName, lastName, '\n', '-'*50,'\n')


    try_again = input("\nTry again? (Press Enter else n to quit)\n ")
    if try_again.lower() == "n":
        break

input("Press Enter to exit.")

