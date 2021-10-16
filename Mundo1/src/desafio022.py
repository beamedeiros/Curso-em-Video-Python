"""Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome. """

"""STRIP = TIRA OS ESPAÇOS"""
nome = input("Digite um nome: ").strip()

"""UPPER = TUDO MAIÚSCULO!!"""
print(f"Seu nome em maiúsculas é {nome.upper()}")

"""LOWER = TUDO MINÚSCULO!!"""
print(f"Seu nome em letras minúsculas é {nome.lower()}")

"""LEN = TOTAL DE LETRAS + ESPAÇO"""
"""COUNT = ELIMINA OS ESPAÇOS ENTRE AS PALAVRAS"""
print(f"Seu nome tem {len(nome)-nome.count(' ')}")


