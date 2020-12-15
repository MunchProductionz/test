# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:33:36 2020

@author: henri
"""

def add_matrix (matrise1, matrise2):
    kolonner = []
    matrise3 = []
    ny_sum = 0
    
    for rad in range(len(matrise1)):
        for kolonne in range(len(matrise1[i])):
            ny_sum = matrise1[rad][kolonne] + matrise2[rad][kolonne]
            kolonner[rad] += [ny_sum]
        matrise3.append(kolonner)
    
    return matrise3