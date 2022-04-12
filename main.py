# -*- coding: utf8 -*
from art import *
from os import system
import time
import platform
import random
import pyperclip as pc


"""
--------------- Antrios ---------------
Ce programme permet de crypter vos phrases. Un
projet qui à débuté en 2017 et qui évolue de
plus en plus. Je serais très contents que l'un
d'entre vous puisse le cracker sans regarder le
code source de ce programme. Voici mon discord
si jamais vous y arrivez : IxemGod#5206.

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
    key = random.randint(len(phrase)+2,len(phrase)+4000000)
    Dicoalphabet = {' ' : 664,'a' : 135,'b' : 208,'c' : 224,'d' : 233,'e' : 782,'f' : 614,'g' : 752,'h' : 274,'i' : 923,'j' : 341,'k' : 648,'l' : 200,'m' : 733,'n' : 745,'o' : 801,'p' : 355,'q' : 603,'r' : 101,'s' : 878,'t' : 407,'u' : 490,'v' : 686,'w' : 995,'x' : 403,'y' : 418,'z' : 896,'A' : 545,'B' : 281,'C' : 588,'D' : 915,'E' : 767,'F' : 338,'G' : 178,'H' : 950,'I' : 788,'J' : 693,'K' : 119,'L' : 503,'M' : 170,'N' : 364,'O' : 310,'P' : 573,'Q' : 622,'R' : 384,'S' : 979,'T' : 232,'U' : 576,'V' : 539,'W' : 600,'X' : 777,'Y' : 817,'Z' : 467,'0' : 102,'1' : 193,'2' : 217,'3' : 848,'4' : 546,'5' : 115,'6' : 516,'7' : 914,'8' : 480,'9' : 959,'!' : 535,'"' : 445,'#' : 288,'$' : 754,'%' : 768,'&' : 190,'\'' : 876,'(' : 626,')' : 156,'*' : 577,'+' : 207,',' : 838,'-' : 575,'.' : 749,'/' : 762,':' : 717,';' : 840,'<' : 593,'=' : 494,'>' : 525,'?' : 640,'@' : 387,'[' : 887,'\\' : 727,']' : 613,'^' : 570,'_' : 185,'`' : 373,'{' : 623,'|' : 196,'}' : 574,'~' : 672}
    dicoNew = {}

    #Un premier alphabet se génères
    for keys,value in Dicoalphabet.items():
        dicoNew[keys] = (value * key)

    key += 1
    resultat = ''
    for lettre in phrase:
        key -= 1
        hexa = str(hex(dicoNew[lettre]*key)+" ")
        resultat += hexa[2:-1]+","

    phrase = str(key)+" "+str(resultat[0:-1])
    return phrase



def decode(phrase,key : int):
    phrase = phrase.split(",")   
    resListeBis = []
    for value in phrase:
        resListeBis.append(int(value,base=16))

    resultat = ""
    DicoNombre = {664 : ' ',135 : 'a',208 : 'b',224 : 'c',233 : 'd',782 : 'e',614 : 'f',752 : 'g',274 : 'h',923 : 'i',341 : 'j',648 : 'k',200 : 'l',733 : 'm',745 : 'n',801 : 'o',355 : 'p',603 : 'q',101 : 'r',878 : 's',407 : 't',490 : 'u',686 : 'v',995 : 'w',403 : 'x',418 : 'y',896 : 'z',545 : 'A',281 : 'B',588 : 'C',915 : 'D',767 : 'E',338 : 'F',178 : 'G',950 : 'H',788 : 'I',693 : 'J',119 : 'K',503 : 'L',170 : 'M',364 : 'N',310 : 'O',573 : 'P',622 : 'Q',384 : 'R',979 : 'S',232 : 'T',576 : 'U',539 : 'V',600 : 'W',777 : 'X',817 : 'Y',467 : 'Z',102 : '0',193 : '1',217 : '2',848 : '3',546 : '4',115 : '5',516 : '6',914 : '7',480 : '8',959 : '9',535 : '!',445 : '"',288 : '#',754 : '$',768 : '%',190 : '&',876 : '\'',626 : '(',156 : ')',577 : '*',207 : '+',838 : ',',575 : '-',749 : '.',762 : '/',717 : ':',840 : ';',593 : '<',494 : '=',525 : '>',640 : '?',387 : '@',887 : '[',727 : '\\',613 : ']',570 : '^',185 : '_',373 : '`',623 : '{',196 : '|',574 : '}',672 : '~'}
    keySup = key + len(resListeBis)-1
    key += len(resListeBis)
    for lettre in resListeBis:
        key -= 1
        resultat += DicoNombre[int((lettre/key)/keySup)]

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
            print(Color.purple_bold+"         [output] "+Color.white_bold+code(phrase)+Color.grey_bold+" (Résultat copié dans le presse-papier)")
            pc.copy(code(phrase))
            fin = input("")
            return


        else:
            print(Color.red_bold+"           [!]"+Color.white_bold+"La phrase à coder doit faire plus de 0 caractère.")
            fin = input("")
            Antrios()


    elif(choix_CodeDecode == 2 or choix_CodeDecode == "2"):

        #On demande la phrase à traiter.
        phrase = input(Color.cyan_bold+"           [?]"+Color.white_bold+" Tapez votre phrase. "+Color.blue_bold)
        key = int(input(Color.cyan_bold+"           [?]"+Color.white_bold+" Tapez votre clée. "+Color.blue_bold))
        if len(phrase) > 0:
            Clears()
            bannier_Antrios()
            print(Color.purple_bold+"         [output] "+Color.white_bold+decode(phrase, key)+Color.grey_bold+" (Résultat copié dans le presse-papier)")
            pc.copy(decode(phrase, key))
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
