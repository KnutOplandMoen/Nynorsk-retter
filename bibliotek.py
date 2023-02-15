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

info = '--------------------------\nHei\n--------------------------\nVelkommen til nynorsk oversetter V2\nFor mer instruks les:\nhttps://github.com/knutmoen123/Nynorsk-retter/blob/main/README.md\n--------------------------'

ordåungå = ['verte', 'vert', 'vart', 'vorte']

hjelpeverb = ['vere', 'vera', 'er', 'var', 'vore', 'verande', 
                'verte', 'verta', 'vert', 'vart', 'vorte', 'vertande',
                'bli', 'blir', 'vart', 'blei', 'blitt', 'vorte', 'blivande']

samsvarsverb = ['vere', 'er', 'var', 'vore',
                'bli', 'blir', 'blei', 'blitt']

eiendomspronomen = ['min','mi','mitt','mine',
                    'din','di','ditt','dine',
                    'hans',
                    'hennes',
                    'dens',
                    'dets',
                    'vår', 'vårt', 'våre',
                    'deres',
                    'sin', 'si', 'sitt', 'sine', 'vÃ¥re'
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

uregelretteverb = { 
    'bere' : ['å bere', 'ber',	'bar', 'har bore']}

averb = [
'danse', 'dansa', 'dansar', 'dansa', 'dansa',	  	
'elske',  'elska', 'elskar', 'elska', 'elska',	  
'filme', 'filma', 'filmar', 'filma', 'filma',	  
'fingre', 'fingra', 'fingrar', 'fingra', 'fingra',   
'fuske', 'fuska', 'fuskar', 'fuska', 'fuska', 	  
'hoppe', 'hoppa', 'hoppar', 'hoppa', 'hoppa',	  
'hugse', 'hugsa', 'hugsar', 'hugsa', 'hugsa',	  
'kaste', 'kasta', 'kastar', 'kasta', 'kasta',	  
'kviskre', 'kviskra', 'kviskrar', 'kviskra', 'kviskra',	  
'lyse', 'lysa', 'lyser', 'lyste', 'lyst',	  
'makte', 'makta', 'maktar',	'makta', 'makta',	  	
'prøve', 'prøva', 'prøver', 'prøvde', 'prøvt', 'prøvd'	  
'rangle', 'rangla', 'ranglar', 'rangla', 'rangla',  
'raspe', 'raspa', 'raspar',	'raspa', 'raspa',	  
'skrubbe', 'skrubba', 'skrubbar', 'skrubba', 'skrubba']

uregelretteverb = [
'eige', 'eiga', 'eig', 'eigde', 'eigt', 'eigd',	  
'gjere', 'gjera', 'gjer', 'gjorde', 'gjort',	  	
'kunne', 'kunna', 'kan', 'kunne', 'kunna',	  	
'leggje', 'leggja', 'legg', 'la', 'lagt',	  
'seie',	'seier', 'sa', 'sagt',	  
'skulle', 'skal', 'skulle', 'skulla',	  
'vilje', 'vil', 'ville', 'vilja',	  
'vite',	'veit', 'visste', 'visst'] 

jverb = ['avtelja', 'avtel', 'avtalde', 'avtalt', 'berja', 'ber', 'barde', 'bart', 'bynja', 'byn', 'bunde', 'bunt', 'drynja', 'dryn', 'drunde', 'drunt', 'dvelja', 'dvel', 'dvalde', 'dvalt', 'dynja', 'dyn', 'dunde', 'dunt', 'dyvja', 'dyv', 'duvde', 'duvd', 'elja', 'el', 'ol', 'ale', 'fintelja', 'fintel', 'fintalde', 'fintalt', 'forselja', 'forsel', 'forselde', 'forselt', 'fortelja', 'fortel', 'fortalde', 'fortalt', 'forvenja', 'forven', 'forvande', 'forvant', 'glymja', 'glym', 'glumde', 'glumt', 'gremja', 'grem', 'gramde', 'gramt', 'grovtelja', 'grovtel', 'grovtalde', 'grovtalt', 'grymja', 'grym', 'grumde', 'grumt', 'hylja', 'hyl', 'hylde', 'hylt', 'kappsymja', 'kappsym', 'kappsumde', 'kappsumt', 'krevja', 'krev', 'kravde', 'kravd', 'kylja', 'kyl', 'kylde', 'kylt', 'lemja', 'lem', 'lamde', 'lamt', 'mylja', 'myl', 'mulde', 'mult', 'myrja', 'myr', 'murde', 'murt', 'oversymja', 'oversym', 'oversumde', 'oversumt', 'overtelja', 'overtel', 'overtalde', 'overtalt', 'rydja', 'ryd', 'rudde', 'rudd', 'rynja', 'ryn', 'runde', 'runt', 'selja', 'sel', 'selde', 'selt', 'semja', 'sem', 'samde', 'samt', 'skilja', 'skil', 'skilde', 'skilt', 'skrynja', 'skryn', 'skrunde', 'skrunt', 'skylja', 'skyl', 'skylde', 'skylt', 'stynja', 'styn', 'stunde', 'stunt', 'symja', 'sym', 'sumde', 'sumt', 'telja', 'tel', 'talde', 'talt', 'temja', 'tem', 'tamde', 'tamt', 'tenja', 'ten', 'tande', 'tant', 'timja', 'tim', 'timde', 'timt', 'turrsymja', 'turrsym', 'turrsumde', 'turrsumt', 'tørrsymja', 'tørrsym', 'tørrsumde', 'tørrsumt', 'underselja', 'undersel', 'underselde', 'underselt', 'urydja', 'uryd', 'urudde', 'urudd', 'utrydja', 'utryd', 'utrudde', 'utrudd', 'velja', 'vel', 'valde', 'valt', 'venja', 'ven', 'vande', 'vant', 'vevja', 'vev', 'vavde', 'vavd', 'ylja', 'yl', 'ulde', 'ult', 'ymja', 'ym', 'umde', 'umt', 'yrja', 'yr', 'urde']

everb = ['abstrahera', 'abstraherer', 'abstraherte', 'abstrahert', 'arbeida', 'arbeider', 'arbeidde', 'arbeidd', 'begynna', 'begynner', 'begynte', 'begynt', 'bygga', 'bygger', 'bygde', 'bygd', 'byggja', 'byggjer', 'bygde', 'bygd', 'byta', 'byter', 'bytte', 'bytt', 'bøya', 'bøyer', 'bøygde', 'bøygt', 'dekkja', 'dekkjer', 'dekte', 'dekt', 'diskutera', 'diskuterer', 'diskuterte', 'diskutert', 'filosofera', 'filosoferer', 'filosoferte', 'filosofert', 'formulera', 'formulerer', 'formulerte', 'formulert', 'frelsa', 'frelser', 'frelste', 'frelst', 'gløyma', 'gløymer', 'gløymde', 'gløymt', 'greia', 'greier', 'greidde', 'greitt', 'gøyma', 'gøymer', 'gøymde', 'gøymt', 'hjelpa', 'hjelper', 'hjelpte', 'hjelpt', 'høyra', 'høyrer', 'høyrde', 'høyrt', 'introdusera', 'introduserer', 'introduserte', 'introdusert', 'kjenna', 'kjenner', 'kjente', 'kjent', 'kjøpa', 'kjøper', 'kjøpte', 'kjøpt', 'knyta', 'knyter', 'knytte', 'knytt', 'konkludera', 'konkluderer', 'konkluderte', 'konkludert', 'kvila', 'kviler', 'kvilte', 'kvilt', 'køyra', 'køyrer', 'køyrde', 'køyrt', 'leia', 'leier', 'leidde', 'leitt', 'leiga', 'leiger', 'leigde', 'leigd', 'leva', 'lever', 'levde', 'levd', 'lø¦ra', 'lø¦rer', 'lø¦rte', 'lø¦rt', 'notera', 'noterer', 'noterte', 'notert', 'nyansera', 'nyanserer', 'nyanserte', 'nyansert', 'presentera', 'presenterer', 'presenterte', 'presentert', 'problematisera', 'problematiserer', 'problematiserte', 'problematisert', 'referera', 'refererer', 'refererte', 'referert', 'reflektera', 'reflekterer', 'reflekterte', 'reflektert', 'reisa', 'reiser', 'reiste', 'reist', 'risikera', 'risikerer', 'risikerte', 'risikert', 'senda', 'sender', 'sende', 'sendt', 'skremma', 'skremmer', 'skremte', 'skremt', 'sleppa', 'slepper', 'sleppte', 'sleppt', 'studera', 'studerer', 'studerte', 'studert', 'styrkja', 'styrkjer', 'styrkte', 'styrkt', 'svekkja', 'svekkjer', 'svekte', 'svekt', 'søla', 'søler', 'sølte', 'sølt', 'tenka', 'tenker', 'tenkte', 'tenkt', 'tenkja', 'tenkjer', 'tenkte', 'tenkt', 'treffa', 'treffer', 'trefte', 'treft', 'trekkja', 'trekkjer', 'trekte', 'trekt', 'tyda', 'tyder', 'tydde', 'tydd', 'variera', 'varierer', 'varierte', 'variert', 'vurdera', 'vurderer', 'vurderte', 'vurdert', 'ynskja', 'ynskjer', 'ynskte']

sterkeverb = ['be', 'ber', 'bad', 'bedt', 'beda', 'bed', 'bad', 'bedd', 'bera', 'ber', 'bar', 'bore', 'bita', 'bit', 'beit', 'bite', 'blåsa', 'blå¦s', 'bles', 'blåse', 'brenna', 'brenn', 'brann', 'brunne', 'bryta', 'bryt', 'braut', 'brote', 'by', 'byr', 'baud', 'bydt', 'byda', 'byd', 'baud', 'bydd', 'drepa', 'drep', 'drap', 'drepe', 'drikka', 'drikk', 'drakk', 'drukke', 'driva', 'driv', 'dreiv', 'drive', 'eta', 'et', 'åt', 'ete', 'fara', 'fer', 'få³r', 'fare', 'finna', 'finn', 'fann', 'funne', 'frysa', 'frys', 'fraus', 'frose', 'få', 'får', 'fekk', 'fått', 'gi', 'gir', 'gav', 'gitt', 'gje', 'gjev', 'gav', 'gjeve', 'gjeva', 'gjev', 'gav', 'gjeve', 'gripa', 'grip', 'greip', 'gripe', 'gråta', 'grå¦t', 'gret', 'gråte', 'gå', 'går', 'gjekk', 'gått', 'halda', 'held', 'heldt', 'halde', 'koma', 'kjem', 'kom', 'kome', 'komma', 'kjem', 'kom', 'komme', 'krypa', 'kryp', 'kraup', 'krope', 'la', 'lar', 'ladde', 'ladt', 'lata', 'låt', 'lå©t', 'late', 'le', 'ler', 'lo', 'lett', 'lesa', 'les', 'las', 'lese', 'lyga', 'lyg', 'laug', 'loge', 'låta', 'lå¦t', 'lå©t', 'låte', 'nyta', 'nyt', 'naut', 'nytt', 'reka', 'rek', 'rak', 'reke', 'rekka', 'rekk', 'rakk', 'rokke', 'ryka', 'ryk', 'rauk', 'roke', 'skina', 'skin', 'skein', 'skine', 'skjera', 'skjer', 'skar', 'skore', 'skrika', 'skrik', 'skreik', 'skrike', 'skriva', 'skriv', 'skreiv', 'skrive', 'skyta', 'skyt', 'skaut', 'skote', 'sleppa', 'slepper', 'sleppte', 'sleppt', 'slita', 'slit', 'sleit', 'slite', 'slå', 'slår', 'slo', 'slege', 'springa', 'spring', 'sprang', 'sprunge', 'stela', 'stel', 'stal', 'stole', 'strekka', 'strekk', 'strakk', 'strokke', 'stå', 'står', 'stod', 'stått', 'svika', 'svik', 'sveik', 'svike', 'synga', 'syng', 'song', 'sunge', 'syngja', 'syng', 'song', 'sunge', 'såkka', 'såkk', 'sokk', 'sokke', 'ta', 'tek', 'tok', 'teke', 'taka', 'tek', 'tok', 'teke', 'tillata', 'tillåt', 'tillå©t', 'tillate', 'vega', 'vegar', 'vega', 'vega', 'veksa', 'veks', 'vaks', 'vakse', 'vera', 'er', 'var', 'vore', 'verta', 'vert', 'vart', 'vorte', 'vinna', 'vinnar', 'vinna']

stverb = ['aldrast', 'aldrast', 'aldrast', 'aldrast', 'ala', 'el', 'ol', 'ale', 'ampa', 'ampar', 'ampa', 'ampa', 'andast', 'andast', 'andast', 'andast', 'anna', 'annar', 'anna', 'anna', 'antra', 'antrar', 'antra', 'antra', 'apa', 'aper', 'apte', 'apt', 'arga', 'argar', 'arga', 'arga', 'arma', 'armar', 'arma', 'arma', 'attrast', 'attrast', 'attrast', 'attrast', 'avdagast', 'avdagast', 'avdagast', 'avdagast', 'avstyggast', 'avstyggest', 'avstygdest', 'avstygst', 'avstyggjast', 'avstyggjest', 'avstygdest', 'avstygst', 'bannast', 'bannast', 'bannast', 'bannast', 'bendast', 'bendest', 'bendest', 'bendst', 'betrast', 'betrast', 'betrast', 'betrast', 'bitast', 'bitst', 'beitst', 'bitest', 'blandast', 'blandast', 'blandast', 'blandast', 'blidkast', 'blidkast', 'blidkast', 'blidkast', 'blygja', 'blygjer', 'blygde', 'blygd', 'brevbytast', 'brevbytest', 'brevbyttest', 'brevbytst', 'brevskiftast', 'brevskiftest', 'brevskiftest', 'brevskifst', 'båyast', 'båyest', 'båygdest', 'båygst', 'dagast', 'dagast', 'dagast', 'dagast', 'devlast', 'devlast', 'devlast', 'devlast', 'dimmast', 'dimmest', 'dimdest', 'dimst', 'djervast', 'djervast', 'djervast', 'djervast', 'doggast', 'doggast', 'doggast', 'doggast', 'dra', 'dreg', 'drog', 'drege', 'druknast', 'druknast', 'druknast', 'druknast', 'dyrkast', 'dyrkast', 'dyrkast', 'dyrkast', 'dåfurdast', 'dåfurdast', 'dåfurdast', 'dåfurdast', 'dåkkast', 'dåkkast', 'dåkkast', 'dåkkast', 'einast', 'einest', 'eintest', 'einst', 'eldast', 'eldest', 'eldest', 'eldst', 'falmast', 'falmast', 'falmast', 'falmast', 'fattast', 'fattast', 'fattast', 'fattast', 'fegnast', 'fegnast', 'fegnast', 'fegnast', 'ferdast', 'ferdast', 'ferdast', 'ferdast', 'finnast', 'finst', 'fanst', 'funnest', 'forfarast', 'forferst', 'forfå³rst', 'forfarest', 'forgå', 'forgår', 'forgjekk', 'forgått', 'forkomast', 'forkjemst', 'forkomst', 'forkomest', 'forkommast', 'forkjemst', 'forkomst', 'forkommest', 'forvitnast', 'forvitnast', 'forvitnast', 'forvitnast', 'furdast', 'furdast', 'furdast', 'furdast', 'fyllast', 'fyllest', 'fyltest', 'fylst', 'fånast', 'fånast', 'fånast', 'fånast', 'fåyrast', 'fåyrast', 'fåyrast', 'fåyrast', 'galnast', 'galnast', 'galnast', 'galnast', 'gantast', 'gantast', 'gantast', 'gantast', 'gi', 'gir', 'gav', 'gitt', 'gje', 'gjev', 'gav', 'gjeve', 'gjerast', 'gjerst', 'gjordest', 'gjorst', 'grynnast', 'grynnest', 'gryntest', 'grynst', 'grånast', 'grånast', 'grånast', 'grånast', 'grånkast', 'grånkast', 'grånkast', 'grånkast', 'grånskast', 'grånskast', 'grånskast', 'grånskast', 'gårast', 'gårast', 'gårast', 'gårast', 'handrekkast', 'handrekkest', 'handrektest', 'handrekst', 'handrekkjast', 'handrekkjest', 'handrektest', 'handrekst', 'handtakast', 'handtekst', 'handtokst', 'handtekest', 'holast', 'holast', 'holast', 'holast', 'holdast', 'holdast', 'holdast', 'holdast', 'hugast', 'hugast', 'hugast', 'hugast', 'hålkast', 'hålkast', 'hålkast', 'hålkast', 'håyrast', 'håyrest', 'håyrdest', 'håyrst', 'idast', 'idest', 'iddest', 'idst', 'ilengast', 'ilengest', 'ilengdest', 'ilengst', 'ilengjast', 'ilengjest', 'ilengdest', 'ilengst', 'illtrivast', 'illtrivst', 'illtreivst', 'illtrivest', 'ilskast', 'ilskast', 'ilskast', 'ilskast', 'kampast', 'kampast', 'kampast', 'kampast', 'kappast', 'kappast', 'kappast', 'kappast', 'kivast', 'kivast', 'kivast', 'kivast', 'kjeftast', 'kjeftast', 'kjeftast', 'kjeftast', 'kjenna', 'kjenner', 'kjente', 'kjent', 'kjeppast', 'kjeppest', 'kjeptest', 'kjepst', 'krevja', 'krev', 'kravde', 'kravd', 'lagast', 'lagast', 'lagast', 'lagast', 'leggjast', 'legst', 'lagdest', 'lagst', 'leiast', 'leiest', 'leiddest', 'leitst', 'lengast', 'lengest', 'lengdest', 'lengst', 'lengjast', 'lengjest', 'lengdest', 'lengst', 'levrast', 'levrast', 'levrast', 'levrast', 'lika', 'liker', 'likte', 'likt', 'likjast', 'likjest', 'liktest', 'likst', 'ljugast', 'lygst', 'laugst', 'logest', 'lognast', 'lognast', 'lognast', 'lognast', 'lukkast', 'lukkast', 'lukkast', 'lukkast', 'lyda', 'lyder', 'lydde', 'lydd', 'lygast', 'lygst', 'laugst', 'logest', 'lykkast', 'lykkast', 'lykkast', 'lykkast', 'låst', 'lå¦st', 'lest', 'låst', 'magrast', 'magrast', 'magrast', 'magrast', 'maktast', 'maktast', 'maktast', 'maktast', 'mannast', 'mannast', 'mannast', 'mannast', 'minnast', 'minnest', 'mintest', 'minst', 'mislukkast', 'mislukkast', 'mislukkast', 'mislukkast', 'mislykkas', 'mislykkas', 'mislykkas', 'mislykkas', 'misminnast', 'misminnest', 'mismintest', 'misminst', 'mistrivast', 'mistrivst', 'mistreivst', 'mistrivest', 'modnast', 'modnast', 'modnast', 'modnast', 'mognast', 'mognast', 'mognast', 'mognast', 'munnhoggast', 'munnhoggest', 'munnhoggdest', 'munnhoggst', 'myklast', 'myklast', 'myklast', 'myklast', 'mådast', 'mådest', 'måddest', 'mådst', 'måtast', 'måtest', 'måttest', 'måtst', 'nappast', 'nappast', 'nappast', 'nappast', 'nebbast', 'nebbast', 'nebbast', 'nebbast', 'nennast', 'nennest', 'nentest', 'nenst', 'nevast', 'nevast', 'nevast', 'nevast', 'nevetakast', 'nevetekst', 'nevetokst', 'nevetekest', 'nåydast', 'nåydest', 'nåyddest', 'nåydst', 'olmast', 'olmast', 'olmast', 'olmast', 'omfarast', 'omferst', 'omfå³rst', 'omfarest', 'omgå', 'omgår', 'omgjekk', 'omgått', 'ordskiftast', 'ordskiftest', 'ordskiftest', 'ordskifst', 'ormektast', 'ormektast', 'ormektast', 'ormektast', 'orminnast', 'orminnest', 'ormintest', 'orminst', 'orvonast', 'orvonast', 'orvonast', 'orvonast', 'ottast', 'ottast', 'ottast', 'ottast', 'pinast', 'pinest', 'pintest', 'pinst', 'pirast', 'pirast', 'pirast', 'pirast', 'pjuskast', 'pjuskast', 'pjuskast', 'pjuskast', 'plagast', 'plagast', 'plagast', 'plagast', 'pårekna', 'påreknar', 'pårekna', 'pårekna', 'reddast', 'reddast', 'reddast', 'reddast', 'rekast', 'rekst', 'rakst', 'rekest', 'rengast', 'rengest', 'rengdest', 'rengst', 'rengja', 'rengjer', 'rengde', 'rengt', 'rennast', 'renst', 'ranst', 'runnest', 'ringast', 'ringast', 'ringast', 'ringast', 'rivast', 'rivst', 'reivst', 'rivest', 'ryggja', 'ryggjer', 'rygde', 'rygd', 'ryktast', 'ryktast', 'ryktast', 'ryktast', 'råkast', 'råkast', 'råkast', 'råkast', 'råmmast', 'råmmest', 'råmdest', 'råmst', 'råynast', 'råynest', 'råyndest', 'råynst', 'samfarast', 'samferst', 'samfå³rst', 'samfarest', 'samstavast', 'samstavast', 'samstavast', 'samstavast', 'seiast', 'seiest', 'sagdest', 'sagst', 'semjast', 'semst', 'samdest', 'samst', 'sjå', 'ser', 'såg', 'sett', 'skilja', 'skil', 'skilde', 'skilt', 'skiplast', 'skiplast', 'skiplast', 'skiplast', 'skjemmast', 'skjemmest', 'skjemdest', 'skjemst', 'skjennast', 'skjennest', 'skjentest', 'skjenst', 'skrankast', 'skrankast', 'skrankast', 'skrankast', 'skrinnast', 'skrinnest', 'skrintest', 'skrinst', 'skumast', 'skumast', 'skumast', 'skumast', 'skymast', 'skymest', 'skymdest', 'skymst', 'slitast', 'slitst', 'sleitst', 'slitest', 'slåst', 'slåst', 'slost', 'slegest', 'slåvast', 'slåvast', 'slåvast', 'slåvast', 'snakka', 'snakkar', 'snakka', 'snakka', 'spårjast', 'spårst', 'spurdest', 'spurst', 'stangast', 'stangast', 'stangast', 'stangast', 'stevjast', 'stevjast', 'stevjast', 'stevjast', 'stortrivast', 'stortrivst', 'stortreivst', 'stortrivest', 'styggast', 'styggest', 'stygdest', 'stygst', 'styggjast', 'styggjest', 'stygdest', 'stygst', 'sykjast', 'sykjest', 'syktest', 'sykst', 'synast', 'synest', 'syntest', 'synst', 'sålast', 'sålast', 'sålast', 'sålast', 'så¦last', 'så¦last', 'så¦last', 'så¦last', 'ta', 'tek', 'tok', 'teke', 'talmast', 'talmast', 'talmast', 'talmast', 'tannast', 'tannast', 'tannast', 'tannast', 'tekka', 'tekker', 'tekte', 'tekt', 'tekkjast', 'tekkjest', 'tektest', 'tekst', 'timast', 'timest', 'timdest', 'timst', 'torast', 'torest', 'tordest', 'torst', 'treffast', 'treffest', 'treftest', 'trefst', 'trengast', 'trengst', 'trongst', 'trungest', 'trivast', 'trivst', 'treivst', 'trivest', 'tufsast', 'tufsast', 'tufsast', 'tufsast', 'turvast', 'tarvst', 'turvtest', 'turvst', 'tvislast', 'tvislast', 'tvislast', 'tvislast', 'tvisynast', 'tvisynest', 'tvisyntest', 'tvisynst', 'tykka', 'tykker', 'tykte', 'tykt', 'tykkjast', 'tykkjest', 'tyktest', 'tykst', 'tynnast', 'tynnast', 'tynnast', 'tynnast', 'tårast', 'tårast', 'tårast', 'tårast', 'tårkast', 'tårkast', 'tårkast', 'tårkast', 'ugjerast', 'ugjerst', 'ugjordest', 'ugjorst', 'uheppast', 'uheppast', 'uheppast', 'uheppast', 'ulagast', 'ulagast', 'ulagast', 'ulagast', 'unast', 'unest', 'untest', 'unst', 'undrast', 'undrast', 'undrast', 'undrast', 'utrivast', 'utrivst', 'utreivst', 'utrivest', 'vantrivast', 'vantrivst', 'vantreivst', 'vantrivest', 'varast', 'varest', 'vardest', 'varst', 'vaslast', 'vaslast', 'vaslast', 'vaslast', 'vederfarast', 'vederferst', 'vederfå³rst', 'vederfarest', 'vemjast', 'vemst', 'vemdest', 'vemst', 'vemmast', 'vemmast', 'vemmast', 'vemmast', 'vitrast', 'vitrast', 'vitrast', 'vitrast', 'vreidast', 'vreidest', 'vreiddest', 'vreidst', 'vrenga', 'vrenger', 'vrengde', 'vrengt', 'vrengjast', 'vrengjest', 'vrengdest', 'vrengst', 'vå¦gjast', 'vå¦gjest', 'vå¦gdest', 'vå¦gst', 'våªrast', 'våªrast', 'våªrast', 'våªrast', 'vånast', 'vånest', 'våntest', 'vånst', 'yllast', 'yllest', 'yltest', 'ylst', 'ylmast', 'ylmest', 'ylmdest', 'ylmst', 'yngast', 'yngest', 'yngdest', 'yngst', 'yngjast', 'yngjest', 'yngdest', 'yngst', 'ynkast', 'ynkast', 'ynkast', 'ynkast', 'yppast', 'yppast', 'yppast', 'yppast', 'yvast', 'yvest', 'yvdest', 'yvst', 'åbyrgjast', 'åbyrgjest', 'åbyrgdest', 'åbyrgst', 'årast', 'årast', 'årast', 'årast', 'å¦ttast', 'å¦ttast', 'å¦ttast', 'å¦ttast', 'ålnast', 'ålnast', 'ålnast', 'ålnast', 'årast', 'årest', 'årdest', 'årst', 'årvå¦nast', 'årvå¦nest', 'årvå¦ntest', 'årvå¦nst', 'åydast', 'åydest', 'åyddest']

kortverb = ['bjå', 'bjår', 'bjådde', 'bjått', 'bla', 'blar', 'bladde', 'bladt', 'ble', 'bler', 'bledde', 'blett', 'blå', 'blår', 'blådde', 'blådt', 'bre', 'brer', 'bredde', 'bredt', 'bry', 'bryr', 'brydde', 'brytt', 'brå', 'brår', 'brådde', 'brått', 'bu', 'bur', 'budde', 'butt', 'by', 'byr', 'baud', 'bydt', 'dy', 'dyr', 'dydde', 'dytt', 'dåy', 'dåyr', 'dåydde', 'dåytt', 'fli', 'flir', 'flidde', 'flitt', 'flu', 'flur', 'fludde', 'flutt', 'fly', 'flyr', 'flydde', 'flytt', 'flå', 'flår', 'flådde', 'flått', 'flå¦', 'flå¦r', 'flå¦dde', 'flå¦tt', 'flå', 'flår', 'flådde', 'flått', 'fri', 'frir', 'fridde', 'fritt', 'frå', 'frår', 'frådde', 'frått', 'få', 'får', 'fådde', 'fådt', 'gjå', 'gjår', 'gjådde', 'gjådt', 'gla', 'glar', 'gladde', 'gladt', 'gle', 'gler', 'gledde', 'gledt', 'glo', 'glor', 'glodde', 'glott', 'glå', 'glår', 'glådde', 'glådt', 'gni', 'gnir', 'gnei', 'gnide', 'gnu', 'gnur', 'gnudde', 'gnutt', 'gny', 'gnyr', 'gnydde', 'gnytt', 'gro', 'gror', 'grodde', 'grott', 'gry', 'gryr', 'grydde', 'grytt', 'grå', 'grår', 'grådde', 'grått', 'grå', 'grår', 'grådde', 'grådt', 'gå', 'går', 'gjekk', 'gått', 'gåy', 'gåyr', 'gåydde', 'gåytt', 'ha', 'har', 'hadde', 'hatt', 'kjå', 'kjår', 'kjådde', 'kjått', 'kle', 'kler', 'kledde', 'kledt', 'kli', 'klir', 'klidde', 'klitt', 'klå', 'klår', 'klådde', 'klått', 'klå', 'klår', 'klådde', 'klått', 'kna', 'knar', 'knadde', 'knatt', 'kny', 'knyr', 'knydde', 'knytt', 'knå', 'knår', 'knådde', 'knådt', 'kri', 'krir', 'kridde', 'kritt', 'kro', 'kror', 'krodde', 'krott', 'kry', 'kryr', 'krydde', 'krytt', 'kvi', 'kvir', 'kvidde', 'kvidt', 'kå', 'kår', 'kådde', 'kått', 'la', 'lar', 'ladde', 'ladt', 'lå', 'lår', 'lådde', 'lådt', 'må', 'mår', 'mådde', 'mått', 'nå', 'når', 'nådde', 'nått', 'ro', 'ror', 'rodde', 'rott', 'ry', 'ryr', 'raud', 'rode', 'rå', 'rår', 'rådde', 'rådt', 'rå', 'rår', 'rådde', 'rått', 'ska', 'skar', 'skadde', 'skadt', 'sko', 'skor', 'skodde', 'skott', 'sky', 'skyr', 'skydde', 'skytt', 'slå', 'slår', 'slådde', 'slått', 'smi', 'smir', 'smidde', 'smidt', 'sno', 'snor', 'snodde', 'snott', 'snu', 'snur', 'snudde', 'snutt', 'snå', 'snår', 'snådde', 'snått', 'spa', 'spar', 'spadde', 'spadt', 'spe', 'sper', 'spedde', 'spett', 'spy', 'spyr', 'spydde', 'spytt', 'ste', 'ster', 'stedde', 'stedt', 'stå', 'står', 'stådde', 'stått', 'sva', 'svar', 'svadde', 'svadt', 'sy', 'syr', 'sydde', 'sytt', 'så', 'sår', 'sådde', 'sått', 'te', 'ter', 'tedde', 'tett', 'tjå', 'tjår', 'tjådde', 'tjått', 'tre', 'trer', 'tredde', 'trett', 'tru', 'trur', 'trudde', 'trutt', 'trå', 'trår', 'trådde', 'trått', 'trå¦', 'trå¦r', 'trå¦dde', 'trå¦dt', 'trå', 'trår', 'trådde', 'trått', 'två', 'tvår', 'tvådde', 'tvått', 'ty', 'tyr', 'tydde', 'tytt', 'tå¦', 'tå¦r', 'tå¦dde', 'tå¦tt', 'tå', 'tår', 'tådde', 'tått', 'urå', 'urår', 'urådde', 'urått', 'va', 'var', 'vadde', 'vadt', 'vri', 'vrir', 'vrei', 'vride', 'vå¦', 'vå¦r', 'vå¦dde']

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
    'boken':'boka',
    'hvorfor':'kvifor',
    'anbefale':'tilrå',
    'begynnelse':'byrjing eller start',
    'mye':'mykje',
    'kjærlighet':'kjærleik',
    'hennes': 'hennar',
    'finnes': 'finst',
    'danser': 'dansar',
    'bøyde': 'bøygde',
    'tok': 'tagde',
    'tatt': 'tagd',
    'velge': 'velje',
    'svømme': 'symje',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    }
