'''Ler um numero inteiro. Se o numero lido for negativo, escreva a mensagem “Numero
invalido”. Se o numero for positivo, calcular o logaritmo deste numero'''

import math

num = int(input("Escolha um número: "))

if num < 0:
    print("Número inválido.")
else:
    print(f"O log de {num} é {math.log10(num)}.")