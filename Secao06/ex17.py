'''
 Faca um programa que leia um numero inteiro positivo  n e calcule a soma dos n primeiros
numeros naturais
'''

n = int(input('Digite um número inteiro e positivo e diferente de 0: '))
soma = 0

while n <= 0:
        print('Número inválido.')
        n = int(input('Digite um número inteiro e positivo e diferente de 0: '))

if n > 0:
    for x in range(n + 1):#capturando numeros no alcance
        soma = soma + x

else:
    print('Número inválido.')
    n = int(input('Digite um número inteiro e positivo e diferente de 0: '))

print('A somar  dos numeros {}' .format(soma))
    