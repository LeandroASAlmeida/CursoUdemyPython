'''17. Leia uma notas 10 x 3 com as notas de 10 alunos em 3 provas. Em seguida, escreva
o numero de alunos cuja pior nota foi na prova 1, o numero de alunos cuja pior nota foi 
na prova 2, e o numero de alunos cuja pior nota foi na prova 3. Em caso de empate 
das piores notas de um aluno, o criterio de desempate e arbitrario, mas o aluno deve ser 
contabilizado apenas uma vez.'''


notas = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
prova1 = float()
prova2 = float()
prova3 = float()

for l in range(0,10):
    for c in range(0,3):
        notas[l][c] = float(input(f"ALUNO {l+1}:\nDigite nota da prova {c+1}: "))
        print('-=' * 30) # linha de separação

for l in range(0,10):
    if min(notas[l]) == notas[l][0]:
        prova1 += 1
        if notas[l][0] == notas[l][1] or notas[l][0] == notas[l][2]:
            prova1 -= 1
    if min(notas[l]) == notas[l][1]:
        prova2 += 1
        if notas[l][1] == notas[l][2]:
            prova2 -= 1
    if min(notas[l]) == notas[l][2]:
        prova3 += 1

print('-=' * 30) # linha de separação
print(f"Número de alunos com a pior nota foi na prova 1: {int(prova1)}\nNúmero de alunos com a  pior nota foi na prova 2: "
      f"{int(prova2)}\nNúmero de alunos com pior nota foi na prova 3: {int(prova3)}")
print('-=' * 30) # linha de separação


   