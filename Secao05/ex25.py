'''Calcule as raızes da equacao de 2 
o grau.
Lembrando que:
x =
−b ±
√
∆
2a
Onde
∆ = B
2 − 4ac
E ax2 + bx + c = 0 representa uma equacao de 2 
o grau.'''

a = float(input('Digite o valor A:'))
b = float(input('Digite o valor B:'))
c = float(input('Digite o valor C:'))

if a == 0:
    print('Não é uma equação de segundo grau.')

delta = (b ** 2) - 4 * a * c
if delta < 0:
    print('Não existe raiz.')
elif delta == 0:
    print(delta ** 0.5, ' - Raiz unica')
else:
    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)
    print('O resultado da equação é: +', x1, 'e', x2)
