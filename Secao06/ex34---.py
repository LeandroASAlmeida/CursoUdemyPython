'''
Faca um programa que calcule o menor numero divisıvel por cada um dos numeros de 1
a 20? Ex: 2520 e o menor numero que pode ser dividido por cada um dos numeros de 1 
a 10, sem sobrar resto.

'''
i = 1
numero = 1

while i != 0:
    if numero % 1 == 0 and numero % 2 == 0 and numero % 3 == 0 and numero % 4 == 0 and numero % 5 == 0 and numero % 6 == 0 and numero % 7 == 0 and numero % 8 == 0 and numero % 9 == 0 and numero % 10:
        print(numero)
        i = 0
    else:
        numero += 1