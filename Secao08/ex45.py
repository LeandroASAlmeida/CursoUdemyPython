'''
44. Faca uma funcao que calcule o desvio padrao de um vetor v contendo n numeros 
Desvio Padrao: 
q 1
n−1
Pn
i=1(v[i] − m)
2
onde m e a media do vetor.
'''
def desvio_padrao(v):

    n = len(v) # numero de itens
    m = sum(v) / len(v) # soma de todos os iens do vetor  dividido pelo numero de itens

    distancia = 0
    for i in v:
        distancia += (i - m) ** 2

    return (distancia / n) ** 0.5

if __name__ == '__main__':
    
    print("Qual será o tamanho do vetor?: ", end=" ")
tam = int(input())
v = []
print("\n")
for i in range(tam):
    print("Informe o ", i+1 ,"° numero do vetor: ", end=" ")
    valor = float(input())
    v.append(valor)
print(f"\nDesvio padrão: {desvio_padrao(v)}")