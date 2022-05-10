'''
60. Escreva uma funcao que compare e retorne verdadeiro, caso uma string seja anagrama 
da outra, e falso, caso contrario.

'''
def anagrama(pA, pB):
    
    if len(pA) != len(pB):
        return "Não e Anagrama"
    elif set(pA) == set(pB):
        return "Verdadeiro"
    else:
        return "Falso"
while True:
    print("Informe a palavra A: ", end=" ")
    A = input()
    print("Informe a palavra B: ", end=" ")
    B = input()
    print(anagrama(A,B))