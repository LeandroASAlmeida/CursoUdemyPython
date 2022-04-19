'''Faça um programa que leia um numero e, caso ele seja positivo, calcule e mostre: 
• O numero digitado ao quadrado 
• A raiz quadrada do numero digitado'''

num = float(input('Informe um numero: '))

if num >= 0:
    nq = num * 2
    rq = num ** 0.5
    print('O numero elevado ao quadrado é :{}'.format(nq))
    print('A raiz quadrada do numero digitado é : {}'.format(rq))
else:
    print('Numero negativo')