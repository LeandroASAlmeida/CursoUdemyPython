'''
66. Faca uma rotina que receba como parametro um vetor de caracteres e seu tamanho. 
A funcao dever a de ler uma string do teclado, caractere por caractere usando a funcao
getchar() ate que o usuario digite enter ou o tamanho maximo do vetor seja alcancado.

'''
def getchar():
  
    caractere = input("Informe um caractere: ")

    if len(caractere) <= 1:
        return caractere


def rotina(s, tamanho):

    for _ in range(tamanho):
        valor = getchar()

        if valor != "":
            s.append(valor)

        else:
            break

    return s


if __name__ == '__main__':
    
    print("Qual será o tamanho do vetor V?: ", end=" ")
    tam = int(input())
    vetor = []

print(f"{rotina(vetor, tam)}")

