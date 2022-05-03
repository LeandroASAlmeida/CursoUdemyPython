'''
10. Faca uma funcao que receba dois numeros e retorne qual deles  e o maior.

'''

def maior(a, b):
    if a > b:
        return f"Maior: {a}"
    return f"Maior: {b}"
print("Informe o 1° numero: ", end=" ")
n1 = float(input())
print("Informe o 2° numero: ", end=" ")
n2 = float(input())
print("\n", maior(n1,n2))
