""" Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep

computador = randint(0,5)
jogador = int(input("De 0 a 5, em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3)
if jogador == computador :
    print("PARABÉNS VOCÊ ACERTOU!")
else :
    print(f"EU PENSEI NO NÚMERO {computador}!")