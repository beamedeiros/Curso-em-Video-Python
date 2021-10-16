import random
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")
lista = [nome1, nome2, nome3]
escolhido = random.choice(lista)
print(f"O escolhido {escolhido}")