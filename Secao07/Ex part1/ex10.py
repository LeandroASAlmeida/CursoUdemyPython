'''
10. Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor,
calcule e imprima a média geral.

'''

indice = 0
vetor = []

while indice < 15:
    nota = float(input(f"Insira a nota ({indice+1}/15): "))
    if 0 < nota < 11: # nota de 0 a 10
        vetor.append(nota)
        indice += 1
    else:
        print("Nota inválida.")

print(f"A média geral entre as quinze notas é de {(sum(vetor) / 15):.2f}.")