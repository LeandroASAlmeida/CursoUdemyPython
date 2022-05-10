'''
41. Faca uma funcao que receba um vetor de reais e retorne a media dele.
'''

def media_num(vetor):
    media= 0
    for i in vetor:
        media += i
    return media / len(vetor)  # retorne a media dividido pelo tam do vetor

if __name__ == '__main__':

    print("Qual será o tamanho do vetor?: ", end=" ")
    tam = int(input())
    vetor = []
    print("\n")
    for i in range(tam):
        print("Informe o ", i+1 ,"° numero do vetor: ", end=" ")
        valor = float(input())
        vetor.append(valor)
    print(f"O media dos elementos do vetor é o", media_num(vetor))

