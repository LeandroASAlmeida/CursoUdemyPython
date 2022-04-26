'''
Faca um programa que receba um numero inteiro maior do que 1, e verifique se o numero 
fornecido e primo ou nao.
'''

num = int(input('Informe um numero inteiro maior do que 1: '))


if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print('{}, NÃO É UM NUMERO PRIMO'.format(num))
            break
        else:
            print('{}, É UM NUMERO PRIMO'.format(num))
            break
else:
    print('{}, NÃO É UM NUMERO PRIMO'.format(num))



















 
