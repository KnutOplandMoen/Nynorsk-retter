from bibliotek import oversetter
from tabulate import tabulate
from bibliotek import averb
from bibliotek import everb
from bibliotek import jverb
from bibliotek import stverb
from bibliotek import uregelretteverb
from bibliotek import kortverb
from bibliotek import sterkeverb 
from bibliotek import samsvarsverb
from bibliotek import hankjonn
from bibliotek import hokjonn
from bibliotek import intetkjonn
from bibliotek import hjelpeverb
from bibliotek import eiendomspronomen
from bibliotek import eiendomspronomenny

eiendomspronomen = eiendomspronomen + eiendomspronomenny
verb = averb + everb + jverb + stverb + uregelretteverb + kortverb + sterkeverb 

def mellom():
    print('\n--------------------------\n')
 
def neste():
    neste = input('Neste ord? ')
    
def ordlik(ord, sjekk):
    if ord == sjekk or ord[:-1] == sjekk or ord[:-2] == sjekk:
        return True

def ordi(word, liste):
    if word in liste:
        return word
    elif word[:-1] in liste:
        return word[:-1] 
    elif word[:-2] in liste:
        return word[:-2]
    else:
        return False

def printfunksjon(ord, typefeil, setning, ordnmr):
    setningtekst = ' '.join(setning)
    if typefeil == 'samsvarhokjonn':
      print(f'Det er blitt funnet en mulig feil setningen:\n"{setningtekst}"\nOrdet: "{ord}" står etter samsvarsverbet: "{setning[ordnmr-1]}" og hokjønns-substantivet: "{setning[ordnmr-2]}"\nDet skal da ofte bøyes med en: "en" ending')
    elif typefeil == 'samsvarhankjonn':
      print(f'Det er blitt funnet en mulig feil setningen:\n"{setningtekst}"\nOrdet: "{ord}" står etter samsvarsverbet: "{setning[ordnmr-1]}" og hankjønns-substantivet: "{setning[ordnmr-2]}"\nDet skal da ofte bøyes med en: "en" ending')
    elif typefeil == 'samsvarintetkjonn':
      print(f'Det er blitt funnet en mulig feil setningen:\n"{setningtekst}"\nOrdet: "{ord}" står etter samsvarsverbet: "{setning[ordnmr-1]}" og intetkjønns-substantivet: "{setning[ordnmr-2]}"\nDet skal da ofte bøyes med en: "e" ending')
    elif typefeil == 'samsvarflertall':
      print(f'Det er blitt funnet en mulig feil setningen:\n"{setningtekst}"\nOrdet: "{ord}" står etter samsvarsverbet: "{setning[ordnmr-1]}" og substantivet: "{setning[ordnmr-2]}"\nDet skal da ofte bøyes med en: "ne" ending\nom substantivet ikke er flertall: søk opp i ordbok')
    elif typefeil == 'genetivs':
        print(f'Det er funnet en mulig feil i setningen:\n"{setningtekst}"\nOrdet: "{ord}" slutter med s, ofte dropper man genetivs s-en i nynorsk.\nOm dette er ett ord som utrykker eieforhold bør du endre det')
    elif typefeil == 'averb':
        print(f'Det er blitt funnet en mulig feil setningen:\n"{setningtekst}"\nOrdet: "{ord}" slutter på "at" eller "de", sjekk at dette er bøyd riktig')
    elif typefeil == 'an':
        print(f'Det er funnet en mulig feil i setningen:\n"{setningtekst}"\nOrdet: "{ord}" starter med "an", ordet kan være feilskrevet, søk det opp i ordboken på nettet')
    elif typefeil == 'be':
        print(f'Det er funnet en mulig feil i setningen:\n"{setningtekst}"\nOrdet: "{ord}" starter med "be", ordet kan være feilskrevet, søk det opp i ordboken på nettet')
    elif typefeil == 'het':
        print(f'Det er funnet en mulig feil i setningen:\n"{setningtekst}"\nOrdet: "{ord}" slutter med "het", ordet kan være feilskrevet, søk det opp i ordboken på nettet')
    elif typefeil == 'else':
        print(f'Det er funnet en mulig feil i setningen:\n"{setningtekst}"\nOrdet: "{ord}" slutter med "else", ordet kan være feilskrevet, søk det opp i ordboken på nettet')
    elif typefeil == 'ligsomending':
        print(f'Det er funnet en mulig feil i setningen:\n"{setningtekst}"\nOrdet: "{ord}" slutter med "lig" eller "som", ordet kan være feilskrevet, søk det opp i ordboken på nettet')
    elif typefeil == 'astending':
        print(f'Det er funnet en mulig feil i setningen:\n"{setningtekst}"\nOrdet: "{ord}" slutter med "ast", det skal da stå ett modalt hjelpeverb før ordet\nFks:\nOppgåva skal/må/bør leverast før helga.')
    
    
def anbehetelsesjekk(ord, setning, ordnmr):
    ord2 = ord.lower()
    if ord2[0:2] == 'an':
        mellom()
        printfunksjon(ord, 'an', setning, '', ordnmr)
        neste()
    
    elif ord2[0:2] == 'be':
        mellom()
        printfunksjon(ord, 'be', setning, '', ordnmr)
        neste()
    
    elif ord2[-4:] == 'else':
        mellom()
        printfunksjon(ord, 'else', setning, '', ordnmr)
        neste()
    
    elif ord2[-3:] == 'het':
        mellom()
        printfunksjon(ord, 'het', setning, '', ordnmr)
        neste()
        
def passiv(ord, setning, ordnmr):
    if ordi(ord, verb):
        if ord[-1:] == 's':
            setningtekst = ' '.join(setning)
            print(f'\nVerbet "{ord}" i setninga:\n\n{setningtekst}\n\nender på -s, dette bør mest sannsynig endre på ved å enten:\n\nEnten bruker du ei form av hjelpeverba bli/verta:\nAlle søknader blir/vert behandla konfidensielt.\nIngen blir/vert kontakta før etter nærare avtale.\n\n2) Eller du legg endinga -ast til stammen av verbet som følgjer etter dei modale hjelpeverba skal/skulle, vil/ville, kan/kunne, må/måtte og bør/burde:')
            neste()
        
        elif ord[-3:] == 'ast': 
            if setning[ordnmr-1] not in hjelpeverb:
                setningtekst = ' '.join(setning)
                print(f'\nfant ikkje eit modalt hjelpeverb før "{ord}" i setninga:\n\n{setningtekst}\n\n som ender på -ast, enten omsrkiv setninga eller legg til eit modalt hjelpeverb før:\n\nDet køyrast for fort … går ikkje\nDet blir køyrt for fort … går')
                neste()  

def sending(ord, setning):
    if ord[-1:] == 's':
        setningtekst = ' '.join(setning)
        print(f'\nVerbet "{ord}" i setninga:\n\n{setningtekst}\n\nender på -s, dette bør mest sannsynig endre på')
              
def ligsomendingsjekk(ord, setning, ordnmr):
    if len(ord) > 3:
        if ord[-3:] == 'lig' or ord[-3:] == 'som':
            mellom()
            printfunksjon(ord, 'ligsomending', setning, ordnmr)
            neste()
            
def eiendomsord(word, setning):
    if word in eiendomspronomen:
        setningtekst = ' '.join(setning)
        print(f'ordet {word} i setninga:\n\n{setningtekst}\n\nmå huskes at skal stå bak substantivet (etterstilt pronomen)')
        neste()
    
def oversettelsesjekk(ord, setning, ordnmr):
    if ord in oversetter:
        mellom()
        setningtekst = ' '.join(setning)
        print(f'\nordet: "{ord}" i setningen:\n"{setningtekst}"\ner det funnet en nynorsk oversettelse til: "{oversetter.get(ord)}"\nOm dette høres feil ut, søk opp ordet i lexin')
        neste()
