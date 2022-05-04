'''
23. Escreva uma funcao que gera um triangulo lateral de altura 2*n-1 e n largura. Por exem- 
plo, a saıda para n = 4 seria:

*
**
***
****
***
**
*

'''

def tri_lat(n):
    for i in range(n):
        print("*" * i)
        
    for i in range(n):
        print("*" * (n - i) )
    return "\n"
print("Informe um numero: ", end=" ")
num = int(input())
print(tri_lat(num))
