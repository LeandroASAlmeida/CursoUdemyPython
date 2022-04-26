'''
Faca um programa que receba dois numeros. Calcule e mostre:
• a soma dos numeros pares desse intervalo de numeros, incluindo os numeros digi- 
tados;
• a multiplicacao dos numeros ımpares desse intervalo, incluindo os digitados;

'''

print('Digite um intervalo')
n1 = int(input('Digite o número : '))
n2 = int(input('Digite o número : '))

soma_pares, multi_impares = 0, 1

for i in range(n1, n2+1):
    if i % 2 == 0:
        soma_pares += i
    else:
        multi_impares *= i

print(f'Soma dos pares: {soma_pares}')
print(f'Multiplicação dos ímpares: {multi_impares}')
