'''
20. Faca um algoritmo que receba um numero inteiro positivo n e calcule o seu fatorial, n!.
'''
def fatorial(n):
    fat = 1
    
    for i in range(1, n+1):
        fat = fat * i
    return fat
print("Informe um numero inteiro: ", end=" ")
num = int(input())
print(f"Fatorial de {num} e {fatorial(num)}")

