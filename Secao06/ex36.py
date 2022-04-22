'''
Faca um programa que calcule a diferenca entre a soma dos quadrados dos primeiros
100 numeros naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez pri- 
meiros numeros naturais  e, 
1
2 + 22 + ... + 102 = 385

O quadrado da soma dos dez primeiros numeros naturais  e, 
(1 + 2 + ... + 10)2 = 552 = 3025
A diferenca entre a soma dos quadrados dos dez primeiros numeros naturais e o qua- 
drado da soma e 3025-385 = 2640.

'''

soma1 = 0
soma2 = 0

for i in range(101): #primeiros 100 numeros naturais
    soma1 += i ** 2 # soma dos quadrados
    soma2 += i

soma2 = (soma2 ** 2) # quadrado da soma

dif = soma2 - soma1 # diferença


print('Soma entre os quadrados: {}'.format(soma1))
print('Quadrado da soma: {}'.format(soma2))
print('Diferença entre o quadrado da soma e a soma dos quadrados: {}'.format(dif))


