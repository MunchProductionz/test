# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:32:29 2020

@author: henri
"""
import random

def car_registration ():
    #opprette skilt
    skilt = ""
    
    #velg 2 random tall fra 65 - 90 (ASCII)
    #omgjør til bokstaver med chr(tall)
    for i in range(2):
        skilt.append(chr(random.randint(65,90)))

    #velg 1 random tall ikke 0
    tall = random.randint(1,9)
    skilt.append(tall)
    
    #velg 4 random tall
    for i in range(4):
        skilt.append(random.randint(0,9))

    #return total
    return skilt
    