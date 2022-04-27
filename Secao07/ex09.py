'''
9. Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre no ecrã os
valores lidos na ordem inversa.
'''



indice = 0
valores = []

while indice < 10:
    num = int(input(f"Digite um valor para o vetor ({indice+1}/10)"))
    if num % 2 == 0: # se for Par
        valores.append(num)
        indice += 1
    else:
        print("Valor inválido!")

print(f"Lista de números pares: {valores}\nLista invertida: {valores[::-1]}") # outro metodo