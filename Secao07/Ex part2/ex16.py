'''16. Faca um programa para corrigir uma prova com 10 questoes de multipla escolha ( a, b,
c, d ou e), em uma turma com 3 alunos. Cada questao vale 1 ponto. Leia o gabarito, e 
para cada aluno leia sua matricula (numero inteiro) e suas respostas. Calcule e escreva: 
Para cada aluno, escreva sua matricula'''


opcoes = ('a', 'b', 'c', 'd', 'e')
respostas = [[], [], []]
gabarito, matriculas, pontuacao = [], [], []

print('Digite os gabarito:')
for l in range(0,10):
    res = ''
    while res not in opcoes:
        res = input(f'{l} - ')
    gabarito.append(res)

print('-=' * 30) # linha de separação
print('Preencha a Matricula do Aluno e depois suas respostas')
print('-=' * 30) # linha de separação
for l in range(0,3):
    pontos = 0
    matriculas.append(int(input(f'Matrícula do Aluno {l}: ')))
    print(f'Respostas do Aluno {matriculas[l]}: ')
    for c in range(10):
        res = ''
        while res not in opcoes:
            res = input(f'{c} - ')
        respostas[l].append(res)

        if respostas[l][c] == gabarito[c]:
            pontos += 1

    pontuacao.append(pontos)

print('-=' * 30) # linha de separação
print('Pontuação final:')
print('-=' * 30) # linha de separação
for l in range(3):
    print(f'Aluno {matriculas[l]}: {pontuacao[l]} pontos.')