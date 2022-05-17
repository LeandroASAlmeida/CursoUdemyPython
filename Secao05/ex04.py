'''Faça um programa que leia um numero e, caso ele seja positivo, calcule e mostre: 
• O numero digitado ao quadrado 
• A raiz quadrada do numero digitado'''

from tkinter import N


num = float(input('Informe um numero: '))

if num >= 0:
    nq = num * 2
    rq = num ** 0.5
    print(f'O numero elevado ao quadrado é :{N}')
    print(f'A raiz quadrada do numero digitado é : {rq}')
else:
    print('Numero negativo')