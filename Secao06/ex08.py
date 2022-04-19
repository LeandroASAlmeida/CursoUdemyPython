'''
Escreva um programa que leia 10 numeros e escreva o menor valor lido e o maior valor 
lido
'''
maior = -99999999999999
menor = 99999999999999

for n in range(10): # contador
    valor = int(input(f"Insira um valor ({n+1}/10):")) # pergunta que entra no laço
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
print('O menor valor é {} e o maior é {}'.format(menor,maior))


