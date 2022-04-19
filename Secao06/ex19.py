'''
Escreva um algoritmo que leia um numero inteiro entre 100 e 999 e imprima na saıda
cada um dos algarismos que compoem o numero
'''


while True:

    num = float(input('Digite um número inteiro entre 100 e 999: '))

    while num < 100 :
        print('Numero Invalido')
        num = int(input('Digite um número inteiro entre 100 e 999: '))

    while num > 999 :
        print('Numero Invalido')
        num = int(input('Digite um número inteiro entre 100 e 999: '))

    if num >= 100 and num <= 999:
        print('O numero digitado foi {}' .format(num))
    print: str(num[0],num[1],num[2])


