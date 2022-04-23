'''Faca um programa que gera um numero aleatorio de 1 a 1000. O usuario deve tentar 
acertar qual o numero foi gerado, a cada tentativa o programa dever a informar se o 
chute e menor ou maior que o numero gerado. O programa acaba quando o usuario 
acerta o numero gerado. O programa deve informar em quantas tentativas o numero foi 
descoberto.

'''

from random import randint

numero = randint(1,1000) # 1 a 1000
cont = 0
acertou = False

while not acertou: #enquanto não acertar o chute faça o loop abaixo.
    print('JOGO DO NUMERO ALEATÓRIO'.center(40,'-'))
    print('Tente Acertar !!!'.center(40,'-'))
    chute= int(input('Chute um numero de 1 a 1000!\n'))
    cont += 1
    if chute == numero:
        acertou = True
    else:
        if chute < numero:
            print(' Errou.. é mais')
        elif chute > numero:
            print('Errou... é menos')

print('Acertou!! o numero escolhido era {}, e você tentou {} vezes'.format(numero,cont))
    
