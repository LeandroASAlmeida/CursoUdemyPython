numero = float(input('Informe um numero real: '))

if numero >= 0:
    rq = numero ** 0.5
    print('O numero digitado é maior que zero e é positivo')
    print('A Raiz quadrada do numero digitado é :{}'.format(rq))
else:
    nq = numero *2
    print('O numero digitado é menor que zero e é negativo')
    print('O valor ao quadrado do numero digitado é: {}'.format(nq))