'''
62. Crie uma funcao que compara duas strings e que retorna se elas sao iguais ou diferentes
'''

def iguais(a, b):
    if a == b:
        return "As palavras são iguais"
    else:
        return "As palavras são diferentes"

if __name__ == '__main__':

    print("Informe a primeira palavras: ", end=" ")
    a = input()
    print("\n\nInforme a segunda palavra: ", end=" ")
    b = input()
    print(f"\n\n {iguais(a,b)}")