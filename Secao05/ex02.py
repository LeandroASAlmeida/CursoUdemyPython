'''Leia um numero fornecido pelo usuario. Se esse numero for positivo, calcule a raiz 
quadrada do numero. Se o numero for negativo, mostre uma mensagem dizendo que o 
numero e invalido.'''


numero = float(input('Informe um valor: '))

if numero > 0:
    rq = numero ** 0.5
    print('A raiz quadrada de {}'.format(numero), 'é : {}'.format(rq))
elif numero <= 0:
    print('NUMERO INVALIDO')

