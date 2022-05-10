'''
65. Faca uma funcao que dado um caractere qualquer retorne o mesmo caractere sempre 
em maiusculo. 
'''


def maiusculo(x):
    return x.upper()
print("Informe uma letra: ", end=" ")
a = input()
print(maiusculo(a[:1]))