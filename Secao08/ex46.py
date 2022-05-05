'''
45. Crie um programa contendo as seguintes funcoes que recebem um vetor V numeros re- 
ais como parametro: 
• Impressao normal do vetor. 
• Impressao inversa. 
• Funcao que retorna a media aritmetica dos elementos do vetor.
'''
def imprimir_normal(args):

    numeros = True
    for i in args:
        if not(type(i) == int or type(i) == float):
            numeros = False

    if numeros:
        print(f"Vetor normal: {args}")
    else:
        print("Apenas números!")


def imprimir_inverso(args):
  

    numeros = True
    for i in args:
        if not(type(i) == int or type(i) == float):
            numeros = False

    if numeros:
        print(f"Vetor inverso: {args[::-1]}")
    else:
        print("Apenas números!")


def media_vetor(args):

    numeros = True
    for i in args:
        if not (type(i) == int or type(i) == float):
            numeros = False

    if numeros:
        return sum(args) / len(args)


imprimir_normal([12, 324, 435.345, 53.65, 34.543, 23.56, 234, 564, 45, 321])
imprimir_inverso([12, 324, 435.345, 53.65, 34.543, 23.56, 234, 564, 45, 321])
print(f"Média aritmética do vetor: {media_vetor([12, 324, 435.345, 53.65, 34.543, 23.56, 234, 564, 45, 321])}")


