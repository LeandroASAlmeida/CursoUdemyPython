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

for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = 1000 - a - b
        if ((a*a) + (b*b)) == (c*c):
            print(a, b, c)



