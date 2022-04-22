'''
Escreva um algoritmo que leia um numero inteiro entre 100 e 999 e imprima na saıda
cada um dos algarismos que compoem o numero
'''

num = float(input('Digite um número inteiro entre 100 e 999: '))

while num < 100 :
    print('Numero Invalido')
    num = int(input('Digite um número inteiro entre 100 e 999: '))

while num > 999 :
    print('Numero Invalido')
    num = int(input('Digite um número inteiro entre 100 e 999: '))

if num >= 100 or num <= 999:
    num = str(num)
    print('O numero digitado foi {}' .format(num))
    print(num[0])
    print(num[1])
    print(num[2])


