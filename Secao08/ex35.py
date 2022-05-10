'''
35. Faca uma funcao nao-recursiva que receba um numero inteiro positivo n e retorne o fatorial quadruplo desse numero. O fatorial quadruplo de um numero n e dado por: 
(2n)!n!


'''

def fatorial_quad(n):
    soma = 1
    fat = 2 * n #(2n)!
    for i in range(1 , fat + 1):
        soma *= i
    fat = 1 #(n!)
    for i in range(1, n+1):
        fat *= i
    return soma / fat

if __name__ == '__main__':

    print("Informe um numero inteiro e positivo: ", end=" ")
    num = int(input())
    print(f"Fatorial quaduplo: {fatorial_quad(num)}")
