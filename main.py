# -*- coding: utf8 -*
from art import *
from os import system
import platform
import pyperclip as pc
import requests
import html


"""
--------------- Antrios ---------------
Ce programme permet de crypter vos phrases. Un
projet qui à débuté en 2017 et qui évolue de
plus en plus. Je serais très contents que l'un
d'entre vous puisse le cracker sans regarder le
code source de ce programme. Voici mon discord
si jamais vous y arrivez : IxemGod.

PS : Une aide sera toujours apportée à ceux qui l'à mérite

-IxemGod
"""

class Color:
    no_colored = "\033[0m"
    white_bold = "\033[1;37m"
    blue_bold = "\033[34m"
    cyan_bold = "\033[1;96m"
    green_bold = "\033[1;92m"
    red_bold = "\033[1;91m"
    yellow_bold = "\033[1;33m"
    orange_bold = "\033[33m"
    purple_bold = "\033[35m"
    pink_bold="\033[95m"
    grey_bold="\033[90m"

def Clears():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")


def bannier_Antrios():
    Clears()
    print(Color.red_bold)
    tprint("Antrios")

def code(phrase):
    key = requests.get("http://90.27.106.27/antrios.php?task=write&value="+phrase).text
    return key



def decode(key):
    resultat = requests.get("http://90.27.106.27/antrios.php?task=decode&value="+key).text
    return resultat

def Antrios():

    bannier_Antrios()
    
    #On demande si l'utilisateur / l'utilisatrice souhaite coder ou décoder un message.
    print(Color.red_bold+" "*17+ "[1] "+Color.white_bold+"""Coder"""+Color.red_bold+" "*11 + "[2] "+Color.white_bold+"""Décoder\n""")
    choix_CodeDecode = input(Color.cyan_bold+" "*11 + "[?]"+Color.white_bold+"Choisis un chifre."+ Color.blue_bold)
    
    bannier_Antrios()

    #On test la réponse du choix de l'utilisateur / l'utilisatrice.
    if choix_CodeDecode == 1 or choix_CodeDecode == "1":
        #On demande la phrase à traiter.
        phrase = input(Color.cyan_bold+"           [?]"+Color.white_bold+" Tapez votre phrase. "+Color.blue_bold)
        if len(phrase) > 0:
            Clears()
            bannier_Antrios()
            response = code(phrase)
            print(Color.purple_bold+"         [output] "+Color.white_bold+response+Color.grey_bold+" (Résultat copié dans le presse-papier)")
            pc.copy(response)
            fin = input("")
            return


        else:
            print(Color.red_bold+"           [!]"+Color.white_bold+"La phrase à coder doit faire plus de 0 caractère.")
            fin = input("")
            Antrios()


    elif(choix_CodeDecode == 2 or choix_CodeDecode == "2"):

        #On demande la phrase à traiter.
        key = input(Color.cyan_bold+"           [?]"+Color.white_bold+" Tapez votre clée. "+Color.blue_bold)
        if len(key) > 0:
            Clears()
            bannier_Antrios()
            response = decode(key)
            print(Color.purple_bold+"         [output] "+Color.white_bold+response+Color.grey_bold+" (Résultat copié dans le presse-papier)")
            pc.copy(response)
            fin = input("")
            return


        else:
            print(Color.red_bold+"           [!]"+Color.white_bold+"La phrase à décoder doit faire plus de 0 caractère.")
            fin = input("")
            Antrios()


    #Si le choix entré est vide ou inexistant.
    else:
        print(Color.red_bold+"           [!]"+Color.white_bold+"Choix Inexistant.")




Antrios()
