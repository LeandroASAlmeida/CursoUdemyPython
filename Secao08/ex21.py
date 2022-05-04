'''21. Escreva uma funcao para determinar a quantidade de numeros primos abaixo N'''

def primos(n):
    numeros = set()
    
    for x in range(1, n):
        for y in range(1, x+1):
            if y == 1 or y == x:
                if y != 1: numeros.add(y)
            elif x % y == 0:
                break
	    
    return numeros
print("Informe um numero inteiro: ", end=" ")
num = int(input())
print("Lista de Numeros Primos: ")
for item in primos(num):
    print(item, end=" ")