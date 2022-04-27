'''
28. Leia 10 numeros inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2.
Copie os valores ımpares de v para v1, e os valores pares de v para v2. Note que cada
um dos vetores v1 e v2 tem no maximo 10 elementos, mas nem todos os elementos sao
utilizados. No final escreva os elementos UTILIZADOS de v1 e v2.

'''

vetor= []
vetor1= []
vetor2= []

print('Digite 10 números inteiros')
for i in range(0,10):
    vetor.append(int(input(f'Digite o {i+1}º número: ')))

    if vetor[i] % 2 != 0:
        vetor1.append(vetor[i])
    else:
        vetor2.append(vetor[i])

print(f'\nVetor: {vetor}')
print(f'\nVetor1: {vetor1}')
print(f'Tamanho {len(vetor1)}')
print(f'\nVetor2: {vetor2}')
print(f'Tamanho {len(vetor2)}')