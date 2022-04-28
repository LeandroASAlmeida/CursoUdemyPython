'''
15. Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando
elementos repetidos.

'''

valores=[]

for n in range(0,20):
    num =int(input('Informe 20 valores: '))
    valores.append(num)
    if valores.count(num) > 1:
       valores.remove(num)
print(f'Lista Limpa {valores}')

