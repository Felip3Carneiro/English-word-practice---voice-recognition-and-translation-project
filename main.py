import random, time
import os

import voz
from ascii import ascii
from palavras import *

lives = 3
fufu = 0
lvl = " "

#Funções

def inicio():
    global lvl

    print(ascii["Olá"])    
    mode = int(input("Escolha uma dificuldade: \n1-Fácil | 2-Médio | 3-Difícil \n"))

    try:
        if mode == 1:
            lvl = "fácil"

        elif mode == 2:
            lvl = "médio"

        elif mode == 3:
            lvl = "difícil"
                
        else:
            print("Tente novamente")
            inicio()

        os.system('cls')
        jogo(lvl)

    except ValueError:
        print("Tente novamente")

def jogo(modo):
    global lives, fufu

    while lives != 0:
        palavra = random.choice(words_by_level[modo])

        print("#" * 20)
        print(f"Palavra sorteada -> { palavra }")
        print("#" * 20)

        fala, certo = voz.falar(palavra)
        
        if certo not in fala:
            print("Perdeu uma vida")
            print(ascii["-1 Vida"])
            lives -= 1

        elif certo in fala:
            print("Parbéns, +10 pontos")
            print(ascii["+10 Pontos"])
            fufu += 10 

        print(f"Vidas restantes = {lives}")
        print(f"Pontuação: {fufu}")

        input("Aperte enter para continuar")
        os.system('cls')

    perdeu()

def perdeu():
    global lives, fufu
    for letra in ascii["Perdeu"]:
        print(letra)
        print(" ")
        time.sleep(0.5)
        
    os.system('cls')
    lives = 3
    fufu = 0
    inicio()

#A partir daqui que começa o que ele vê
inicio()