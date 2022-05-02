'''Leia uma matriz 5 x 10 que se refere respostas de 10 questoes de multipla escolha, 
referentes a 5 alunos. Leia tambem um vetor de 10 posicoes contendo o gabarito de 
respostas que podem ser a, b, c ou d. Seu programa devera comparar as respostas 
de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo a
pontuacao correspondente a cada aluno.'''

respostas = [[],[],[],[],[]]
gabarito = ('a', 'b', 'c', 'd')
acertos= []
pontos = [0, 0, 0, 0, 0]

for l in range(0,5):
    print(f'Digite as respostas do Aluno:{l}: ')
    for c in range(0,10):
        res = ''
        while res not in gabarito:
            res = input(f'{c}: ')
        respostas[l].append(res)

print('-=' * 30) # linha de separação
print('\nDigite as respostas corretas')
print('-=' * 30) # linha de separação

for l in range(0,10):
    res = ''
    while res not in gabarito:
        res = input(f'{l}: ')
    acertos.append(res)

for l in range(0,5):
    for c in range(0,10):
        if acertos[c] == respostas[l][c]:
            pontos[l] += 1


print('\nPontuação final')
print('-=' * 30) # linha de separação

for l in range(0,5):
    print(f'Aluno {l}: {pontos[l]} pontos.')
    print('-=' * 30) # linha de separação
for c in range(0,5):
    for c in range(0,10):
        print(f'[{respostas[l][c]:^5}]', end ='')