'''
 Faca uma funcao nao-recursiva que receba um numero inteiro positivo n e retorne o fatorial exponencial desse numero. Um fatorial exponencial e um inteiro positivo n elevado
a pot ` encia de n − 1, que por sua vez e elevado  a pot ` encia de  n − 2 e assim em diante.
Ou seja:
n
(n−1)(n−2)...


'''

def expo_fat(n):
   x = 1
   for i in range(n-1):
        x *=  n ** n-i
   return x

print("Informe um numero inteiro e positivo: ", end=" ")
num = int(input())
print(f"HiperFatorial: {expo_fat(num)}")

