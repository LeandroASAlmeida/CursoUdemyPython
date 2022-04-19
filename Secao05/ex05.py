'''Faca um programa que receba um numero inteiro e verifique se este numero  e par ou 
impar'''

num = int(input('Informe um valor: '))
resto = num % 2 # RESTO É IGUAL O NUMERO DIGITADO DIVIDIDO POR 2 -SE O O RESTO DESSE DIVISÃO FOR IGUAL A "0"

if resto == 0:
    print('Numero digitado é par')
else:
    print('Numero digitado é impar')