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
def desvio_padrao(args):

    n = len(args)
    m = sum(args) / len(args)

    distancia = 0
    for i in args:
        distancia += (i - m) ** 2

    return (distancia / n) ** 0.5


print(f"\nDesvio padrão: {desvio_padrao([22, 324, 34, 23, 2432, 3443, 323.43, 345.45, 43.54, 34.8])}")