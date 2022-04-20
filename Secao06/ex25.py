'''
Faca um programa que some todos os numeros naturais abaixo de 1000 que sao multiplos 
de 3 ou 5
'''

num=int(input('Digite o numero 1000: '))
soma = 0
cont = 0

while num != 1000:
    print('Eu pedi para digitar 1000')
    num=int(input('Digite o numero 1000: '))

if num == 1000:
    for n in range(1000):
        if n % 3 == 0 or n % 5 == 0:
            soma = soma + n # acumulador = acumulando os valores
            cont = cont + 1 # contador = vai contando os valores

print('A soma dos numero multipos por 3 ou 5 é {}.'.format(soma))
print('Foram achados {} numeros multipos por 3 ou 5.'.format(cont))


