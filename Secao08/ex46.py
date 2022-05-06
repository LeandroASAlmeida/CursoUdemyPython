'''
45. Crie um programa contendo as seguintes funcoes que recebem um v V numeros re- 
ais como parametro: 
• Impressao normal do v. 
• Impressao inversa. 
• Funcao que retorna a media aritmetica dos elementos do v.
'''
def imprimir_normal(v):

    valor = True
    for i in v:
        if not(type(i) == int or type(i) == float):
            valor = False

    if valor:
        print(f"Imprimir_normal : {v}")
    else:
        print("Apenas números!")


def imprimir_inverso(v):
  

    valor = True
    for i in v:
        if not(type(i) == int or type(i) == float):
            valor = False

    if valor:
        print(f"Imprimir_inverso : {v[::-1]}")
    else:
        print("Apenas números!")
        

def media_v(v):

    valor = True
    for i in v:
        if not (type(i) == int or type(i) == float):
            valor = False

    if valor:
        print(f"A media aritmetica do v é : {sum(v) / len(v)}")
       

if __name__ == '__main__':
    
    print("Qual será o tamanho do vetor V?: ", end=" ")
tam = int(input())
v = []

for i in range(tam):
    print("Informe o ", i+1 ,"° numero do vetor V: ", end=" ")
    valor = float(input())
    v.append(valor)
imprimir_normal(v)
imprimir_inverso(v)
media_v(v)


