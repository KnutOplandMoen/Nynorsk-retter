# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:18:37 2022

main fil 

@author: knmoa
"""
import sprakfunksjoner as sf

original = '«Jeg har vært inspirert av Ibsen i alle bøkene mine, men særlig her» sier Marit Eikemo til NRK under ett intervju angående lanseringen av hennes nye roman; «gratis og uforpliktande verdivurdering» i 2018. Ibsen er kjent for å skildre hvordan samfunnsmessige problemer og utfordringer påvirker livet til mennesker. Dette ser man i Ibsens 1881 drama; «Gjengangere», der han fremstiller datidens samfunn på en svært direkte og kontroversiell måte. Dramaet omhandler blant annet en mor som ønsker å skape seg en fasade om en god familie, når familien i realiteten ikke er helt perfekt. Det samme gjør Eikemo i sin roman, over 100 år senere. Dette gjør det spennende å sammenligne disse to verkene, sett i lys av sin tid. Hva skjer når vi later som at familielivet er perfekt, og denne fasaden faller?'#'Komikar, skribent og kunststudent Gunhild Dahlberg publiserte fredag 8. februar 2013 en kronikk på dagbladet sine nettsider (Dahlberg, 2016). I denne kronikken, som er skreve som satire, parodierer Dahlberg nett hets av profilerte kvinner. Gjennom teksten kjem Dahlberg med fleire idear til hat mail som ho kunne ha skreve til diverse profilerte menn i Noreg. Desse mailane inneheld språkbruk som, som sjølv sagt av Dahlberg, nokon kanskje vil finne for slemt, for drygt og kanskje til og med uakseptabelt (Dahlberg, 2016). Det er derimot akkurat dette Dahlberg ønskjer å få frem gjennom sin kronikk: At profilerte kvinner får netthets som er for slem, for dryg og uakseptabel. '
nytekst  = '\n'

oversettning = True
if oversettning:
    print('oversetting i konsoll er på, skriv j eller J for å oversette når det blir spurt om')

setninger = original.split('.')

for setningnmr in range(len(setninger)):
    setning = setninger[setningnmr].split()
    setninger = sf.eiendomssjekk(ord, setning, oversettning, setninger, setningnmr)  
    setning = setninger[setningnmr].split()
    ordnmr = -1
    for ord in setning:
        lengde = len(setning)
        ordnmr +=1
        
        komma = False 
        punktum = False

        if ord[-1] == ',':
            komma = True
            ord = ord[:-1]
        elif ord[-1] == '.':
            punktum = True
            ord = ord[:-1]  
        
        ord = sf.oversettelsesjekk(ord, setning, oversettning, ordnmr)
        
        ord = sf.anbehetelsesjekk(ord, setning, oversettning, ordnmr) 
        
        ord = sf.ligendingsjekk(ord, setning, oversettning, ordnmr)
        
        ord = sf.ssjekk(ord, setning, oversettning, ordnmr)
        
        ord = sf.astendingsjekk(ord, setning, oversettning, ordnmr)
        
        ord = sf.samsvarsbøyning(ord, setning, ordnmr, oversettning)
        
        
        if komma:
            ord += ','
        elif punktum:
            ord += '.'

        if ordnmr == 0:
            ord = list(ord)
            ord[0] = ord[0].upper()
            ord = ''.join(ord)
            
        if ordnmr == lengde:
            nytekst += ord + '. '
        else:
            nytekst += ord + ' '
          
    
sf.mellom()
print('original tekst:', original)
sf.mellom()
print('oversatt tekst:', nytekst)    