'''
24. Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o segundo representando a sua altura em metros.
Encontre o aluno mais baixo e o mais alto. Mostre o número do aluno mais baixo e do
mais alto, juntamente com suas alturas.

'''

alunos = {} 
maisalto = 0

for aluno in range(0,10):
    altura = float(input(f"Digite a altura do aluno {aluno+1}: "))
    alunos[aluno] = altura
print(alunos)

for i, j in alunos.items():
    if j == max(alunos.values()):
        print(f"O aluno mais alto é o de número {i}, medindo {j}")
    if j == min(alunos.values()):
        print(f"O aluno mais baixo é o de número {i}, medindo {j}")

