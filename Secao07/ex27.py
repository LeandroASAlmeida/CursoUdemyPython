'''
27. Leia 10 numeros inteiros e armazene em um vetor. Em seguida escreva os elementos 
que sao primos e suas respectivas posicoes no vetor. 

'''

vetor=[]
primos=[]
posicoes = []

print('Digite 10 números inteiros')
for i in range(0,10):
    vetor.append(int(input(f'Digite o {i+1}º número: ')))
    if (vetor[i] % 2 != 0) and (vetor[i] != 1):
        cont = 0
        for j in range(1, vetor[i]):
            if vetor[i] % j == 0:
                cont += 1
            if cont > 2:
                break
        if cont < 2:
            primos.append(vetor[i])
            posicoes.append(i)

print('Números primos no vetor')
for i in range(len(primos)):
    print(f'vetor[{posicoes[i]}] = {primos[i]}')