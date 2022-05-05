'''
40. Faca uma funcao que receba um vetor de inteiros e retorne o maior valor

'''
def maior_num(vetor):
    maior= 0
    for i in vetor:
        if  i > maior:
            maior = i
    return maior


print("Qual será o tamanho do vetor?: ", end=" ")
tam = int(input())
vetor = []
print("\n")
for i in range(tam):
    print("Informe o ", i+1 ,"° numero do vetor: ", end=" ")
    valor = int(input())
    vetor.append(valor)
print(f"O maior elemento da lista é o", maior_num(vetor))

