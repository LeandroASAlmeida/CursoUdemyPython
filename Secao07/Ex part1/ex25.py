'''
25. Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros
naturais que não são múltiplos de 7 ou que terminam com 7.
'''

num = 1
contador = 0
vetor = []

while contador < 100:
    if num % 7 != 0 and str(num)[-1] != '7':
        vetor.append(num)
        contador += 1
    num+= 1
print(vetor)
print(len(vetor))