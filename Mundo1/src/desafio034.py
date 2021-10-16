"""  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

sal = float(input('Digite seu salário: R$'))

if sal <= 1250 :
    novo_sal = sal + (sal * 0.015)
    print(f'Seu novo salário é R${novo_sal}')
else :
    novo_sal = sal + (sal * 0.01)
    print(f'Seu novo salário é R${novo_sal}')

