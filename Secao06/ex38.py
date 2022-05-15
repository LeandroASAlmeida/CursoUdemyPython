'''
. Faca um programa que calcule o terno pitagorico  a, b, c, para o qual a+b+c = 1000. Um
terno pitagorico  e um conjunto de tres numeros naturais, a, b, c, para a qual,
a
2 + b
2 = c
2
Por exemplo,
3
2 + 42 = 9 + 16 = 25 = 52

'''
from math import sqrt # sqrt() é uma função embutida na linguagem de programação Python que retorna a raiz quadrada de qualquer número.

a = float(input("Informe o valor de a: "))
if a.is_integer():
    a = int(a)

b = float(input("Informe o valor de b: "))
if b.is_integer():
    b = int(b)

x = sqrt((a**2) + (b**2))
if x.is_integer():
    x = int(x)

if isinstance(x, int):
    print(x)
else:
    print("Não é terno pitagórico")
