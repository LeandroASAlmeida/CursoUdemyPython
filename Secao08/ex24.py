'''
24. Escreva uma funcao que gera um triangulo de altura e lados n e base 2*n-1. Por exem- 
plo, a saıda para n = 6 seria:
     *
    ***
   *****
  *******
 *********
***********

'''

def triangulo(n):
    for i in range(-1,n*2+1,2):
        print(" " * int(((n*2)-i)/2),end=" ")
        print("*" * i)
    return "\n"

if __name__ == '__main__': #checagem de escopo de execução

    print("Informe um numero: ", end=" ")
    num = int(input())
    print(triangulo(num))
