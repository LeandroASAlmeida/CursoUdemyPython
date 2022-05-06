'''
 Faca uma funcao nao-recursiva que receba um numero inteiro positivo  n e retorne o hiperfatorial desse numero. O hiperfatorial de um numero n, escrito H(n), e definido por: 
H(n) = Qn
k=1 k
k = 11
· 2
2
· 3
3
. . .(n − 1)n−1
· n
n


'''

def hiper_fat(n):
   x = 1
   for i in range(1, n+1):
        x = x * (i ** i)
        return x
print("Informe um numero inteiro e positivo: ", end=" ")
num = int(input())
print(f"HiperFatorial: {hiper_fat(num)}")


