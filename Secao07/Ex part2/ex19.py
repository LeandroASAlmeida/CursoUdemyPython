'''19. Faca um programa que leia uma matriz de 5 linhas e 4 colunas contendo as seguintes
informacoes sobre alunos de uma disciplina, sendo todas as informacoes do tipo inteiro: 
• Primeira coluna: numero de matrıcula (use um inteiro)
• Segunda coluna: media das provas 
• Terceira coluna: media dos trabalhos 
• Quarta coluna: nota final
Elabore um programa que:

(a) Leia as tres primeiras informacoes de cada aluno 
(b) Calcule a nota final como sendo a soma da media das provas e da media dos 
trabalhos
(c) Imprima a matrıcula do aluno que obteve a maior nota final (assuma que so existe 
uma maior nota)
(d) Imprima a media aritmetica das notas finais'''

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
tipo = 0
soma = 0
media_aritmetica = 0
maior_nota = 0


for l in range(0,5):
    matriz[l][0] = int(input(f"ALUNO {l+1}\nInforme seu número de matrícula:"))
print('-=' * 30) # linha de separação
for l in range(0,5):
    matriz[l][1] = int(input(f"ALUNO {l+1}\nInforme a média de suas provas:"))
print('-=' * 30) # linha de separação
for l in range(0,5):
    matriz[l][2] = int(input(f"ALUNO {l+1}\nInforme a média de seus trabalhos:"))
print('-=' * 30) # linha de separação
for l in range(0,5):
    matriz[l][3] = matriz[l][1] + matriz[l][2]


for l in range(0,5):
    for c in range(0,4):
        if c == 0:
            tipo = 'MATRICULA'
        if c == 1:
            tipo = 'MÉDIA PROVAS'
        if c == 2:
            tipo = 'MÉDIA TRABALHOS'
        if c == 3:
            tipo = 'NOTA FINAL'
        print(f"ALUNO {l+1} - {tipo}:  [{matriz[l][c]:^3}] ", end=' ')
    print( )


for l in range(5):
    soma += matriz[l][3]
    media_aritmetica = soma / 5
print(f"\nMédia Aritmética: {media_aritmetica}")




