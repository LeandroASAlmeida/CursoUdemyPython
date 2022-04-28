'''
37. Considere um vetor A com 11 elementos onde A1 < A2 < · · · < A6 > A7 > A8 >
· · · > A11, ou seja, esta ordenado em ordem crescente ate o sexto elemento, e a partir 
desse elemento esta ordenado em ordem decrescente. Dado o vetor da questao anterior, 
proponha um algoritmo para ordenar os elementos.

'''

vetor_a =[]
cont = 0

while cont < 11:
    valor = int(input(f"Digite um valor para o vetor A({cont+1}/11): "))
    if valor in vetor_a:
        print("Este número já foi digitado anteriomente! Digite outro número.")
    else:
        vetor_a.append(valor)
        cont += 1

vetor_a.sort()
vetorordenado = vetor_a[5:11] + vetor_a[0:5][::-1]
print(vetorordenado)



