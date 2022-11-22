# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 17:53:22 2022

språkfunksjoner 

@author: knmoa
"""
from bibliotek import substantiv
from bibliotek import oversetter 
from bibliotek import hokjonn
from bibliotek import hankjonn
from bibliotek import intetkjonn
from bibliotek import eiendomspronomen
from bibliotek import eiendomspronomenny
from bibliotek import hankjonnpronomen
from bibliotek import intetkjonnpronomen
from bibliotek import hokjonnpronomen
from bibliotek import samsvarsverb

def mellom():
    print('\n--------------------------\n')

def ordendring(ord, setning, oversettning):
    if oversettning:
        oversette = input('vil du endre dette nå? ').upper()
        if oversette == 'J':
            ord = input('\nSkriv inn det nye ordet som skal byttes: ')

    return ord

def ordi(ord, liste):
    if ord in liste or ord[:-1] in liste or ord[:-2] in liste:
        return True
    else:
        return False
        
def ordikkei(ord, liste):
    if ord in liste or ord[:-1] in liste or ord[:-2] in liste:
        return False
    else:
        return True
    
def markereordnmr(ordnmr, setningliste):
    setningliste2 = setningliste
    setningliste2[ordnmr] = setningliste2[ordnmr].upper()
    return(' '.join(setningliste2))
    
'''
def setningsendring(type, setningnmr, setninger, eiendomspronomen, setning, oversettning):
    for word in setning:
        if type == 'eiendomsord':
            if word in eiendomspronomen:
                mellom()
                print('\nsetningen:\n', ' '.join(setning), '\ninneholder eiendomsordet "', word,'" husk at dette skal være etter substantiv')
                if oversettning:
                    oversette = input('vil du endre dette nå? ').upper()
                    if oversette == 'J':
                        setninger[setningnmr] = input('Skriv den nye setningen: ')
                        setninger[setningnmr].split()
    return setninger
'''
   
def anbehetelsesjekk(ord, setning, oversettning, ordnmr):
    ord2 = ord.lower()
    if ord2[0:2] == 'an':
        mellom()
        print('\nordet:\n\n', ord, '\n\ni setningen:\n\n', markereordnmr(ordnmr, setning), '\n\nstarter med an, sjekk ordbok')
        ord = ordendring(ord, setning, oversettning)
    
    elif ord2[0:2] == 'be':
        mellom()
        print('\nordet:\n\n', ord, '\n\ni setningen:\n\n', markereordnmr(ordnmr, setning), '\n\nstarter med be, sjekk ordbok')
        ord = ordendring(ord, setning, oversettning)
    
    elif ord2[-4:] == 'else':
        mellom()
        print('\nordet:\n\n', ord, '\n\ni setningen:\n\n', markereordnmr(ordnmr, setning), '\n\nslutter med else, sjekk ordbok')
        ord = ordendring(ord, setning, oversettning)
    
    elif ord2[-3:] == 'het':
        mellom()
        print('\nordet:\n\n', ord, '\n\ni setningen:\n\n', markereordnmr(ordnmr, setning), '\n\nslutter med het, sjekk ordbok')
        ord = ordendring(ord, setning, oversettning)

    return ord
        
def ligendingsjekk(ord, setning, oversettning, ordnmr):
    if ord[-3:] == 'lig':
        mellom()
        print('\nordet:\n\n', ord, '\n\ni setningen:\n\n', markereordnmr(ordnmr, setning), '\n\nslutter med lig, skal det heller være leg her?')
        ord = ordendring(ord, setning, oversettning)
        
    return ord

def astendingsjekk(ord, setning, oversettning, ordnmr):
    if ord[-3:] == 'ast':
        mellom()
        print('\nordet:', ord, 'i setningen:\n', markereordnmr(ordnmr, setning), '\nslutter med ast, husk at det skal være ett modalt hjelpever før ordet, fks\nOppgåva skal/må/bør leverast før helga.')
        ord = ordendring(ord, setning, oversettning)
        
    return ord

'''
def eiendomspronomensjekk(ord, setning, oversettning, eiendomspronomen, oversetter):
    if ord in eiendomspronomen:
        if ord in oversetter:
            mellom()
            riktigord = oversetter.get(ord)
            print('\ndet er ett eiendomspronom skrevet på bokmål:', ord, 'i setningen:\n', setning, '\nskal det her heller være:', riktigord, ',og sjekk at dette er etter substandtiv')
            ord = ordendring(ord, setning)      
        else:
            mellom()
            print('\ndet er ett eiendomspronom:', ord, 'i setningen:\n', ' '.join(setning), '\nsjekk at dette er etter substandtiv')
            ord = ordendring(ord, setning)
            
    return ord
'''

def oversettelsesjekk(ord, setning, oversettning, ordnmr):
    if ord in oversetter:
        mellom()
        print('\nordet:\n\n', ord, 'i setningen:\n\n',markereordnmr(ordnmr, setning),'\n\ner det funnet en nynorsk oversettelse til:\n\n', oversetter.get(ord), '\n\n om dette høres feil ut, søk opp ordet i lexin')
        ord = ordendring(ord, setning, oversettning)
    return ord  

def ssjekk(ord, setning, oversettning, ordnmr):
    if ord[-1:] == 's':
        mellom()
        print('\nordet:\n\n', ord, '\n\ni setningen:\n\n', markereordnmr(ordnmr, setning), '\n\ner det funnet s på slutten.\nOrd på nynorsk med s på slutten skal ofte endres\nfks: bokmal: bygdas folk, nynorsk: folket i bygda')
        ord = ordendring(ord, setning, oversettning)
    return ord

def eiendomsforelleretter(setning, setninger, setningnmr, ordnmr, lengde, kjonn, kjonntekst, kjonnpronomen, kjonn2, kjonn2pronomen, kjonn3, kjonn3pronomen):
    if ordi(setning[ordnmr-1], kjonn) or ordi(setning[ordnmr-2], kjonn):
        print(setning[ordnmr])
        print('hei')
        if setning[ordnmr] in kjonn2pronomen:
            print('ordet:\n\n', setning[ordnmr],'\n\ner ett pronomen av annet kjønn en substantivet, det står etter ett',kjonntekst,'substantiv, skal det heller være ett av disse?:\n\n',
                  kjonnpronomen,'som skal stå i setningen:\n\n',markereordnmr(ordnmr, setning),'\n\nhusk at da også substantivet må bøyes, fks:\nsin roman -> romanEN sin')
            oversette = input('vil du endre dette nå? ').upper()
            if oversette == 'J':
                setning[ordnmr] = input('Skriv nytt ord: ')
                setninger[setningnmr] = setning
                
        elif setning[ordnmr] in kjonn3pronomen:
            print('ordet:', setning[ordnmr],'er ett pronomen av annet kjønn en substantivet, det står etter ett',kjonntekst,'substantiv, skal det heller være ett av disse?:\n',
                  kjonnpronomen,'som skal stå i setningen:\n',markereordnmr(ordnmr, setning),'\nhusk at da også substantivet må bøyes, fks:\nsin roman -> romanEN sin')
            oversette = input('vil du endre dette nå? ').upper()
            if oversette == 'J':
                setning[ordnmr] = input('Skriv nytt ord: ')
                setninger[setningnmr] = setning
            
    elif ordnmr < lengde: 
          if ordi(setning[ordnmr+1], kjonn):
             if setning[ordnmr] in kjonn2pronomen:
                 print('ordet:',setning[ordnmr],'er ett pronomen av annet kjønn en substantivet, det står før ett',kjonntekst,'substantiv, skal det heller være ett av disse?:\n',
                       kjonnpronomen,'som skal stå i setningen:\n',markereordnmr(ordnmr, setning),'\nhusk at da også substantivet må bøyes, fks:\nsin roman -> romanEN sin')
                 oversette = input('\nvil du endre dette nå? ').upper()
                 if oversette == 'J':
                     setninger[setningnmr] = input('Skriv den nye setningen: ')
                     print(setninger)
                     
             elif setning[ordnmr] in kjonn3pronomen:
                 print('ordet:',setning[ordnmr],'er ett pronomen av annet kjønn en substantivet, det står før ett',kjonntekst,'substantiv, skal det heller være ett av disse?:\n',
                       kjonnpronomen,'som skal stå i setningen:\n',markereordnmr(ordnmr, setning),'\nhusk at da også substantivet må bøyes, fks:\nsin roman -> romanEN sin')
                 oversette = input('\nvil du endre dette nå? ').upper()
                 if oversette == 'J':
                     setninger[setningnmr] = input('Skriv den nye setningen: ')
             
             else:
                 print('ordet:', setning[ordnmr],'er ett pronomen, og står før ett',kjonntekst,'substantiv, skal det heller stå etter substantivet i setningen:\n',markereordnmr(ordnmr, setning),'\nhusk at da også substantivet må bøyes, fks:\nsin roman -> romanEN sin')
                 oversette = input('\nvil du endre dette nå? ').upper()
                 if oversette == 'J':
                     setninger[setningnmr] = input('Skriv den nye setningen: ')
      

    return setninger

def eiendomssjekk(ord, setning, oversettning, setninger, setningnmr):
    ordnmr = -1
    lengde = len(setning)
    for ord in setning:
        ordnmr +=1
        
        if ord in eiendomspronomen and ord in oversetter:
            mellom()
            print('\nordet:', ord, 'i setningen:\n', ' '.join(setning), '\ner ett eiendomsord som er funnet i bokmålslista, skal det heller være:', oversetter.get(ord),'?')
            ord = ordendring(ord, setning, oversettning)
            
        elif ord in eiendomspronomenny or ord in eiendomspronomen:
            mellom()  
            setninger = eiendomsforelleretter(setning, setninger, setningnmr, ordnmr, lengde, hokjonn, 'hokjonn', hokjonnpronomen, hankjonn, hankjonnpronomen, intetkjonn, intetkjonnpronomen)
            setninger = eiendomsforelleretter(setning, setninger, setningnmr, ordnmr, lengde, hankjonn, 'hankjonn', hankjonnpronomen, hokjonn, hokjonnpronomen, intetkjonn, intetkjonnpronomen)
            setninger = eiendomsforelleretter(setning, setninger, setningnmr, ordnmr, lengde, intetkjonn, 'intetkjonn', intetkjonnpronomen, hokjonn, hokjonnpronomen, hankjonn, hankjonnpronomen)
          
    return setninger
   
def samsvarsbøyning(ord, setning, ordnmr, oversettning):
    if setning[ordnmr-1] in samsvarsverb and ordnmr != len(setning)-1 and ordikkei(ord, substantiv):

            
        if ordi(setning[ordnmr-2], hankjonn) or ordi([ordnmr-2], hankjonn) and ord[-2:] != 'en':
            mellom()
            print('\nordet:\n',ord,'\ni setningen:\n', ' '.join(setning), '\nstår etter etter verbet:\n',setning[ordnmr-1],'\nog substantivet:\n', setning[ordnmr-2], 'det skal da bøyes med en "en" ending da dette er hunkjonn')
            ord = ordendring(ord, setning, oversettning)
            
        elif ordi(setning[ordnmr-2], hankjonn) or ordi([ordnmr-2], hankjonn) and ord[-2:] != 'en':
            mellom()
            print('\nordet:\n',ord,'\ni setningen:\n', ' '.join(setning), '\nstår etter etter verbet:\n',setning[ordnmr-1],'\nog substantivet:\n', setning[ordnmr-2], '\ndet skal da bøyes med en "en" ending da dette er hankjonn')
            ord = ordendring(ord, setning, oversettning)
        
        
        elif ordi(setning[ordnmr-2], intetkjonn) or ordi([ordnmr-2], intetkjonn) and ord[-1:] != 'e':
            mellom()
            print('\nverbet:\n',ord,'\ni setningen:\n', ' '.join(setning), '\nstår etter etter verbet:\n',setning[ordnmr-1],'\nog substantivet:\n', setning[ordnmr-2], '\ndet skal da bøyes med en "e" ending da dette er intetkjonn')
            ord = ordendring(ord, setning, oversettning)
        else:
            mellom()
            print('\nverbet:\n',ord,'\ni setningen:\n', ' '.join(setning), '\nstår etter etter verbet:\n',setning[ordnmr-1],'\nog substantivet:\n', setning[ordnmr-2], '\ndet skal da bøyes med en "ne" ending om det er bak ett flertall substantiv, om det ikke er flertall: slå opp!')
            ord = ordendring(ord, setning, oversettning)
            
    return ord
    
    