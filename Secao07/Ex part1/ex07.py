'''
7. Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.


'''
valores=[]

for n in range(0,10):
    num =int(input('Informe 10 valores inteiros: '))
    valores.append(num)
print(valores)

print(f"O maior elemento da lista é o {max(valores)}\nPosicionado no indice {valores.index(max(valores))}.")