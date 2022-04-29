'''Leia uma matriz 5 x 10 que se refere respostas de 10 questoes de multipla escolha, 
referentes a 5 alunos. Leia tambem um vetor de 10 posicoes contendo o gabarito de 
respostas que podem ser a, b, c ou d. Seu programa devera comparar as respostas 
de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo a
pontuacao correspondente a cada aluno.'''

matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for l in range(5):
    for c in range(10):
        matriz[l][c] = int(input(f'Digite um valor para a Matriz 0 [{l},{c}]: '))