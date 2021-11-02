# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:14:50 2021

@author: Antoine
"""

noms = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
valeurs = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

#J'enlève la couleur, car elle n'a pas d'impact sur le jeu
Dist = {"Alice": ["Nine", "King", "Five", "Ace", "Three", "Four", "Two", "Two", "Seven", "Eight", "Three", "Ten", "Nine", "Seven", "Two", "Queen", "Two", "Nine", "Ten", "Five", "Eight", "Queen", "Three", "Four", "Jack", "King"], "Bob": ["Five", "Eight", "Six", "Jack", "Four", "Seven", "Five", "Eight", "Jack", "King", "Nine", "Ten", "Six", "Ace", "Queen", "Three", "Seven", "Jack", "Six", "King", "Six", "Ace", "Queen", "Ace", "Four", "Ten"]}

#Transformation de la valeurs de chaque carte
Dist = {"Alice": ["9", "13", "5", "14", "3", "4", "2", "2", "7", "8", "3", "10", "9", "7", "2", "12", "2", "9", "10", "5", "8", "12", "3", "4", "11", "13"], "Bob": ["5", "8", "6", "11", "4", "7", "5", "8", "11", "13", "9", "10", "6", "14", "12", "3", "7", "11", "6", "13", "6", "14", "12", "14", "4", "10"]}

Dist[0].values()
Dist["Alice"]
Dist["Bob"]

gain = []
iteration = 0
#
for carte in Dist.values() :
    #Je pose cette première condition qui me renvoi 0 si Alice n'apparaît plus dans le dictionnaire
    if Dist.get("Alice",0) == 0 :
        print("Bob", iteration)
    #Même principe pour Bob
    elif Dist.get("Bob",0) == 0 :
        print("Alice", iteration)  
    #Si les deux sont encore dans le dictionnaire le jeu continue
    else : 
        carteAlice = Dist["Alice"][carte]
        carteBob = Dist["Bob"][carte]
    
        NewcardA = carteAlice
        NewcardB = carteBob
    
        if carteAlice > carteBob :
            gain = Dist.pop(carteAlice, carteBob)
            Dist["Alice"].append(gain)
        elif carteAlice < carteBob : 
            gain = Dist.pop(carteAlice, carteBob)
            Dist["Bob"].append(gain)
        else :
            while NewcardA == NewcardB :
                gain = Dist.pop(carteAlice, carteBob)
                gain = Dist.pop(Dist["Alice"][1],Dist["Bob"][1])
                NewcardA = Dist["Alice"].pop[1]
                NewcardB = Dist["Bob"].pop[1]
                if NewcardA > NewcardB :
                    gain = Dist.pop(carteAlice, carteBob)
                    Dist["Alice"].append(gain)
                elif NewcardA < NewcardB : 
                    gain = Dist.pop(carteAlice, carteBob)
                    Dist["Bob"].append(gain)
    iteration = iteration + 1






