'''
18. Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os
múltiplos de um número inteiro x num vetor e mostre-os no ecrã.


'''

valores=[]
multiplos=[]


for n in range(0,10):
   num =int(input('Informe 10 valores: '))
   valores.append(num)

x = x = int(input('Digite o valor de x: '))

for num in valores:
    if num % x == 0:
        multiplos.append(num)

print(f'Números digitados que são múltiplos de {x}: \n{set(multiplos)}')
