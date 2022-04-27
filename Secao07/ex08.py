'''
8. Crie um programa que lê 6 valores inteiros e, em seguida, mostre no ecrã os valores
lidos na ordem inversa.
'''

valores=[]

for n in range(0,6):
    num =int(input('Informe 6 valores inteiros: '))
    valores.append(num)
print(valores)

valores.reverse()
print(valores)