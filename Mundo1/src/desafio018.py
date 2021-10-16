import math
angulo = float(input("Digite o ângulo: "))
cos = math.cos(math.radians(angulo))
print(f"O cosseno do ângulo {angulo} é {cos:.2f}")
sen = math.sin(math.radians(angulo))
print(f"O seno do ângulo {angulo} é {sen:.2f}")
tan = math.tan(math.radians(angulo))
print(f"A tangente do ângulo {angulo} é {tan:.2f}")