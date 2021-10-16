"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

n = int(input("Digite um número: "))
resultado = n % 2

if resultado == 1 :
    print("Seu número é ímpar!")
else :
    print("Seu número é par!")