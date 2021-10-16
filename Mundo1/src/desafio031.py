""" Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

km = float(input("Qual a distância em km? "))
if km <= 200:
    passagem = 0.50 * km
    print(f"Sua passagem é: {passagem}")
elif km > 200:
    passagem = 0.45 * km
    print(f"Sua passagem é: {passagem}")
