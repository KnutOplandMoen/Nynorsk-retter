# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 13:58:48 2023

program for innhenting av ordlister fra fks: https://www.dinordbok.no/verb/nynorsk/lister/regelrette-verb/
kopier hele tabellen inn i ord.txt fil

@author: knmoa
"""

jverb = open('ord.txt', 'r').read().split('\n')

nyliste = []
for i in jverb:
    i = i.split(' ')

    for n in i:
        if n != '' and n != '/' and n != 'Infinitiv\tPresens\tPreteritum\tPresens' and n != 'perfektum\t' and len(n) > 1 and n[0] not in ['0', '1', '2','3', '4', '5', '6', '7', '8', '9']:
            n = n.split(' ')
            ord = ''
            for i in n[0]:
                if i == 'Ã':
                    i = 'ø'
                if i == '¸':
                    i = ''
                if i == 'ø':
                    i = 'å'
                if i == '¥':
                    i = ''
                if i == 'å¨':
                    i = 'e'
                if i == '¨':
                    i = ''
                    
                if i == '\t':
                    nyliste.append(ord)
                    ord = ''
                else:
                    ord += i
                
        
                
            
print(nyliste)