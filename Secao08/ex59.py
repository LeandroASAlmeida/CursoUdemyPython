'''
58. Faca uma funcao que recebe, por parametro, 2 vetores de 10 elementos inteiros e que 
calcule e retorne, tambem por parametro, o vetor uniao dos dois primeiros.
'''
import random

def uniao(a,b):
    c = set(a+b)
    return list(c)
A = []
B = []

for i in range(10):
    A.append(random.randrange(1,999))
    B.append(random.randrange(1,999))
print("Vetor A: ", A,"\n\n")
print("Vetor B: ", B,"\n\n")
print("União: ",uniao(A,B))