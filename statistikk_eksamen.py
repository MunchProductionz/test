# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:40:42 2020

@author: henri
"""

def eksamen_statistikk(eksamener):
    
    #Definisjoner
    len_eksamener = len(eksamener)
    oppgave_kapittel = []
    
    #Kapitler
    kapitler = [
        '1 ',
        '2 ',
        '3 ',
        '4 ',
        '5 ',
        '6 ',
        '7 ',
        '9 ',
        '18 '
        ]
    
    #Counts
    count_kap_1 = 0
    count_kap_2 = 0
    count_kap_3 = 0
    count_kap_4 = 0
    count_kap_5 = 0
    count_kap_6 = 0
    count_kap_7 = 0
    count_kap_9 = 0
    count_kap_18 = 0
    
    #Legger alle oppgaver i 1 liste
    for i in range(len_eksamener):
        oppgave_kapittel += eksamener[i]
 
    #Teller kapittel
    for oppgave in oppgave_kapittel:
        
        #Kapittel 1
        if oppgave == 1:
            count_kap_1 += 1
        
        #Kapittel 2
        elif oppgave == 2:
            count_kap_2 += 1
            
        #Kapittel 3
        elif oppgave == 3:
            count_kap_3 += 1
            
        #Kapittel 4
        elif oppgave == 4:
            count_kap_4 += 1
            
        #Kapittel 5
        elif oppgave == 5:
            count_kap_5 += 1
            
        #Kapittel 6
        elif oppgave == 6:
            count_kap_6 += 1
            
        #Kapittel 7
        elif oppgave == 7:
            count_kap_7 += 1
            
        #Kapittel 9
        elif oppgave == 9:
            count_kap_9 += 1
        
        #Kapittel 18
        elif oppgave == 18:
            count_kap_18 += 1
        
        else:
            pass
        
    #Utregning %    
    antall_oppgaver = len(oppgave_kapittel)
    
    prosent_kap_1 = str(int((count_kap_1 / antall_oppgaver) * 100)) + '% - '
    prosent_kap_2 = str(int((count_kap_2 / antall_oppgaver) * 100)) + '% - '
    prosent_kap_3 = str(int((count_kap_3 / antall_oppgaver) * 100)) + '% - '
    prosent_kap_4 = str(int((count_kap_4 / antall_oppgaver) * 100)) + '% - '
    prosent_kap_5 = str(int((count_kap_5 / antall_oppgaver) * 100)) + '% - '
    prosent_kap_6 = str(int((count_kap_6 / antall_oppgaver) * 100)) + '% - '
    prosent_kap_7 = str(int((count_kap_7 / antall_oppgaver) * 100)) + '% - '
    prosent_kap_9 = str(int((count_kap_9 / antall_oppgaver) * 100)) + '% - '
    prosent_kap_18 = str(int((count_kap_18 / antall_oppgaver) * 100)) + '% - '
    
    #Oversikt kapitler
    oversikt = {
        kapitler[0]: prosent_kap_1,
        kapitler[1]: prosent_kap_2,
        kapitler[2]: prosent_kap_3,
        kapitler[3]: prosent_kap_4,
        kapitler[4]: prosent_kap_5,
        kapitler[5]: prosent_kap_6,
        kapitler[6]: prosent_kap_7,
        kapitler[7]: prosent_kap_9,
        kapitler[8]: prosent_kap_18
        }
    
    #Printer oversikt
    for key, val in oversikt.items():
        print(key, val)
    print()
 
k_2020 = [4,5,4,6,6,9,9,1,7,1,18]
h_2019 = [4,5,2,3,4,6,6,7,18,9,1]
k_2019 = [4,5,6,2,18,4,9,7,1,2,7]       
h_2018 = [4,5,18,6,1,6,9,4,6,6,2,7]
k_2018 = [1,3,1,2,5,5,7,9,9,1,18,5,7]
h_2017 = [4,1,4,3,4,7,2,5,5,9,18,5,6]
k_2017 = [5,4,1,6,7,18,1,9,9]
h_2016 = [6,3,4,1,3,7,4,6,9,6,18]
k_2016 = [4,18,5,1,7,4,9,4,4,2,7]
h_2015 = [4,5,18,2,4,6,7,7,1,9,6,9]
k_2015 = [6,2,7,5,4,9,7,6,1,5]
h_2014 = [6,1,2,5,2,4,7,2,9,9]
k_2014 = [1,1,2,7,6,9,2,1,7,6,7,18,6]
h_2013 = [2,5,2,4,4,7,9,7,9]
k_2013 = [1,2,4,3,7,9]
h_2012 = [1,9,2,7,3,4,6,7,18]
k_2012 = [1,1,6,7,1,18,2,4,4]
h_2011 = [1,4,4,4,18,5,18,5,6,9]
k_2011 = [4,4,1,4,18,9,6,18]
h_2010 = [1,4,2,7,7,5,18,5,9,6]
k_2010 = [1,7,5,4,4,9,6,9,18]

eksamen_alle = [k_2020, k_2019, h_2019, k_2018, h_2018, k_2017, h_2017, k_2016, h_2016, h_2015, k_2015, h_2014, k_2014, h_2013, k_2013, h_2012, k_2012, h_2011, k_2011]
eksamen_høst = [k_2020, k_2019, k_2018, k_2017, k_2016, k_2015, k_2014, k_2013, k_2012, k_2011]
eksamen_kont = [h_2019, h_2018, h_2017, h_2016, h_2015, h_2014, h_2013, h_2012, h_2011]

eksamen_statistikk(eksamen_høst)


