'''
8. Sejam a e b os catetos de um triangulo, onde a hipotenusa  e obtida pela equacao: 
hipotenusa =
√
a
2 + b
2. 
Faca uma funcao que receba os valores de a e b e calcule o
valor da hipotenusa atraves da equacao. 

'''
import math

def hipotenusa(a, b):
    h = math.sqrt((a**2 + b**2))
    return h
print("Informe o cateto A: ", end=" ")
a = int(input())
print("Informe o cateto b: ", end=" ")
b = int(input())
print(f"\n Hipotenusa = {hipotenusa(a, b)}")
