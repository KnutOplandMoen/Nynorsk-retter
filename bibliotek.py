# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:13:42 2022

bibliotek

@author: knmoa
"""

hokjonn = open('hokjonn.txt', 'r').read().split('\n') #https://no.wiktionary.org/wiki/Kategori:Hunkj%C3%B8nnsord_i_nynorsk

hankjonn = open('hankjonn.txt', 'r').read().split('\n')  #https://no.wiktionary.org/wiki/Kategori:Hunkj%C3%B8nnsord_i_nynorsk

intetkjonn = open('intetkjonn.txt', 'r').read().split('\n')  #https://no.wiktionary.org/wiki/Kategori:Intetkj%C3%B8nnsord_i_nynorsk

substantiv = hankjonn + hokjonn + intetkjonn

uregelrettsubstantiv = open('uregelrettsubstantiv.txt', 'r').read().split('\n')  #https://no.wiktionary.org/wiki/Kategori:Substantiv_i_nynorsk_med_uregelrett_flertallsb%C3%B8yning


samsvarsverb = ['vere', 'vera', 'er', 'var', 'vore', 'verande', 
                'verte', 'verta', 'vert', 'vart', 'vorte', 'vertande',
                'bli', 'blir', 'vart', 'blei', 'blitt', 'vorte', 'blivande']



eiendomspronomen = ['min','mi','mitt','mine',
                    'din','di','ditt','dine',
                    'hans',
                    'hennes',
                    'dens',
                    'dets',
                    'vår', 'vårt', 'våre',
                    'deres',
                    'sin', 'si', 'sitt', 'sine'
                    ]

eiendomspronomenny = ['min','mi','mitt','mine',
                    'din','di','ditt','dine',
                    'hans',
                    'hennar',
                    'hens',
                    'dess',
                    'vår', 'vårt', 'våre',
                    'dykkar', 'dokkar', 'deira'
                    'sin', 'si', 'sitt', 'sine']
                    
hankjonnpronomen = ['min', 'din', 'vår', 'sin']
hokjonnpronomen = ['mi', 'di', 'vår', 'si']
intetkjonnpronomen = ['mitt', 'ditt', 'vårt', 'sitt']  
flertallpronomen = ['mine', 'dine', 'våre', 'sine']                  

oversetter = {
    'man': 'ein', 
    'gjør': 'gjer',
    'ikke': 'ikkje',
    'være': 'vere',
    'vært': 'vore',
    'ble':'blei eller vart',
    'bare': 'berre',
    'de': 'dei',
    'en': 'ein',
    'et': 'eit', 
    'noe': 'noko',
    'noen': 'nokon',
    'tro': 'tru',
    'bo': 'bu',
    'fikk': 'fekk',
    'vei': 'veg',
    'sted': 'EIN stad',
    'fortsatt': 'framleis',
    'vei': 'veg',
    'finnes':'finst', 
    'sier': 'seier',
    'si': 'seie',
    'jeg': 'eg',
    'da': 'då',
    'snillere': 'snillare',
    'snilleste': 'snillaste',
    'plutselig': 'plutseleg',
    'åpen': 'open',
    'åpne': 'opne',
    'hvis': 'viss/dersom',
    'kommer': 'kjem',
    'alene': 'åleine',
    'hver': 'kvar',
    'hvert': 'kvart',
    'leke': 'leike',
    'sammen': 'saman',
    'spise':'ete',
    'gikk':'gekk',
    'holder':'held',
    'holdt':'heldt',
    'forteller':'fortel',
    'fortelle':'fortelje',
    'fortalte':'fortalde',
    'skrev':'skreiv',
    'skriver':'skriv',
    'hjem':'heim',
    'hvit':'kvit',
    'hva':'kva',
    'hverandre':'kvarandre',
    'mandag':'måndag',
    'ansatt':'tilsett',
    'trengs':'trengst',
    'ellers':'elles',
    'traff':'trefte',
    'potensiale':'potensial',
    'ilag':'i lag',
    'meinar':'meiner',
    'mener':'meiner',
    'fins': 'finst',
    'eksempel':'til dømes',
    'se':'sjå',
    'følelse':'kjensle',
    'fra':'frå',
    'hvordan':'korleis',
    'hvem':'kven',
    'dere':'de om før verb',
    'hun':'ho',
    'leser':'les',
    'leste':'las',
    'skriver':'skriv',
    'lest':'lese',
    'skrevet':'skrive',
    'disse':'desse',
    'dessa':'desse',
    'deia':'desse',
    'allerede':'allereie/alt',
    'ett':'eitt',
    'forfatter':'forfattar',
    'fremdeles':'framleis/enno',
    'gammel':'gammal/gamal',
    'gang':'gong (om tid)',
    'boken':'boka'
    }