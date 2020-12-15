# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:29:15 2020

@author: henri
"""

import random

def randomGruppeGen(bois, ikke_bois):
    
    antall_bois = len(bois)
    antall_ikke_bois = len(ikke_bois)
    
    gruppe_bois = []
    gruppe_ikke_bois = []
    
    for i in range(antall_bois):
        person = bois[(random.randint(0, antall_bois - 1))]
        
        if person not in gruppe_bois:
            gruppe_bois.append(person)
        else:
            while person in gruppe_bois:
                person = bois[(random.randint(0, antall_bois - 1))]
            
            gruppe_bois.append(person)
            
    
    for i in range(antall_ikke_bois):
        person = ikke_bois[(random.randint(0, antall_ikke_bois - 1))]
        
        if person not in gruppe_ikke_bois:
            gruppe_ikke_bois.append(person)
        else:
            while person in gruppe_ikke_bois:
                person = ikke_bois[(random.randint(0, antall_ikke_bois - 1))]
            
            gruppe_ikke_bois.append(person)
    
    print(gruppe_bois)
    print(gruppe_ikke_bois)
    
    gruppe_1 = [gruppe_bois[0], gruppe_ikke_bois[0], gruppe_ikke_bois[1]]
    gruppe_2 = [gruppe_bois[1], gruppe_ikke_bois[2], gruppe_ikke_bois[3]]
    gruppe_3 = [gruppe_bois[2], gruppe_ikke_bois[4]]
    
    print(f'Gruppe 1 er {gruppe_1}')
    print(f'Gruppe 2 er {gruppe_2}')
    print(f'Gruppe 3 er {gruppe_3}')
    
bois = ['Erik', 'Vetle', 'Henrik']
ikke_bois = ['Sara', 'Thea', 'Emilie', 'Synne', 'Selma']

randomGruppeGen(bois, ikke_bois)