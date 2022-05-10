'''
59. Escreva uma funcao que retorne a primeira posicao de uma sub-string dentro de uma 
string. Caso a sub-string nao seja encontrada, a funcao deve retornar -1.

'''
def string(palavra):
    
    if type(palavra) != str:
        return -1
    return palavra[0:1]

if __name__ == '__main__':
    
    print("Informe uma palavra: ", end=" ")
    p = input()
    print(f"\n\n Sub-String: {string(p)}")