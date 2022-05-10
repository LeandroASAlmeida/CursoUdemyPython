'''
. Faca uma funcao que receba um vetor de inteiros e retorne quantos valores pares ela
possui.

'''
def vetor_pares(vetor):

    cont = 0
    for i in vetor :
        if i % 2 == 0:
            cont +=1
    return cont
if __name__ == '__main__':

    print("Qual será o tamanho do vetor?: ", end=" ")
    tam = int(input())
    vetor = []
    print("\n")
    for i in range(tam):
        print("Informe o ", i+1 ,"° numero do vetor: ", end=" ")
        valor = int(input())
        vetor.append(valor)
    print("\n Tem ",vetor_pares(vetor)," numero(s) Par(es) no Vetor")



