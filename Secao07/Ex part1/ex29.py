'''
Faca um programa que receba 6 numeros inteiros e mostre:
• Os numeros pares digitados; 
• A soma dos numeros pares digitados; 
• Os numeros ımpares digitados;
• A quantidade de numeros ımpares digitados;

'''

vetor=[]
pares=[]
soma_pares=0
impares=[]
quart_impar=0

for i in range(6):
    vetor.append(int(input(f'Digite o {i+1}º número: ')))

    if vetor[i] % 2 == 0:
        pares.append(vetor[i])
        soma_pares += vetor[i]
    else:
        impares.append(vetor[i])
        quart_impar += 1

print(f'Os Números pares digitados: {pares}')
print(f'A Soma dos pares: {soma_pares}')
print(f'Os Números ímpares digitados: {impares}')
print(f'A Quantidade de ímpares: {quart_impar}')
