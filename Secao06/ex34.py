'''
Faca um programa que calcule o menor numero divisıvel por cada um dos numeros de 1
a 20? Ex: 2520 e o menor numero que pode ser dividido por cada um dos numeros de 1 
a 10, sem sobrar resto.

'''
menor = 0
cont = 0

for i in range(1, 999999):

    for j in range(1, 16):
        if i % j == 0:
            cont += 1

        if cont >= 15:
            men = i

    if menor > 0:
        print(menor)
        break

    cont = 0