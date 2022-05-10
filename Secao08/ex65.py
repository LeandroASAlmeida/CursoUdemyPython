'''
64. Implemente a funcao a qual recebe duas strings,  str1 e str2, e um valor inteiro positivo
N. A funcao concatena nao mais que N caracteres da string apontada por str2 a string `
apontada por str1 e termina str1 com NULL.
'''

def somar(str1, str2, n):
    if n > len(str1):
        str2 += str1[::]
        str1 = None
        
    else:
        str2 += str1[0:n]
        str1 = None
    return [str1,str2]

if __name__ == '__main__':

    print("Informe um numero inteiro positivo: ", end=" ")
    num = int(input())
    print("\nPrimeira palavras: ", end=" ")
    a = input()
    print("\nSegunda Palavra: ", end=" ")
    b = input()
    print(f"\n\nStr1: {somar(a,b,num)[0]}")
    print(f"\n\nStr2: {somar(a,b,num)[1]}")