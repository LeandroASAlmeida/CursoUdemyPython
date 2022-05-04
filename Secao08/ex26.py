'''
26. Faca um algoritmo que receba um numero inteiro positivo  n e calcule o somatorio de 1 
ate n.

'''
def somatorio(n):
    x=0
    for i in range(1,n + 1):
        x += i
    return x
print("Informe um numero inteiro: ", end=" ")
num = int(input())
print(f"Somatoria: {somatorio(num)}")

