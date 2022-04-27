'''
13. Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se
encontram o maior e o menor valor.

'''

valores=[]

for n in range(0,5):
    num =int(input('Informe 5 valores: '))
    valores.append(num)
print(valores)

print(f"O maior elemento da lista é o {max(valores)}\nPosicionado no indice {valores.index(max(valores))}.")
print(f"O menor elemento da lista é o {min(valores)}\nPosicionado no indice {valores.index(min(valores))}.")