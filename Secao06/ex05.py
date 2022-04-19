'''Faca um programa que peca ao usuario para digitar 10 valores e some-os'''


soma= 0

for n in range (10):
    valor = int(input('Insira um valor ({}/10): '.format(n+1)))
    soma = soma + valor
print('A soma dos valores é {}' .format(soma))




