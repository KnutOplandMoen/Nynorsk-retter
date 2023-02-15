# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:45:57 2023

@author: knmoa
"""
import funksjonerV4 as f4
from bibliotek import info

original = open('tekst.txt','r')
original = original.read()

print(info)
#start = input('starte sjekking av tekst? ')
print('\n--------------------------\nStarter sjekking av tekst...\n--------------------------')

setninger = original.split('.')

for setningnmr in range(len(setninger)):
    setning = setninger[setningnmr].split()
    ordnmr = -1
    for ord in setning:
        ord = ord.lower()
        ordnmr += 1
        setningtekst = ' '.join(setning)
        lengde = len(setning)

        if ord[-1] == ',':
            komma = True
            ord = ord[:-1]
        elif ord[-1] == '.':
            punktum = True
            ord = ord[:-1]  
        
        f4.passiv(ord, setning, ordnmr)
        f4.ligsomendingsjekk(ord, setning, ordnmr)
        f4.eiendomsord(ord, setning)
        
        
        
        #må få opp alle feil med ett ord på en gang, så kunne trykke seg til neste ord
    
print('\nFerdig med tekst')
