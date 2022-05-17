'''Leia um numero real. Se o numero for positivo imprima a raiz quadrada. Do contrario, 
imprima o numero ao quadrado'''


numero = float(input('Informe um numero real: '))

if numero >= 0:
    rq = numero ** 0.5
    print(f'O numero digitado é maior que zero e é positivo')
    print(f'A Raiz quadrada do numero digitado é :{rq}')
else:
    nq = numero *2
    print(f'O numero digitado é menor que zero e é negativo')
    print(f'O valor ao quadrado do numero digitado é: {nq}')