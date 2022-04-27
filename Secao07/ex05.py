'''
5. Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
'''

valores=[]
cont =0

for n in range(0,10):
    num =int(input('Informe 10 valores inteiros: '))
    valores.append(num)
print(valores)

for num in valores:
    if num % 2 == 0:
        cont += 1

print(f"O vetor {valores} possui {cont} elementos pares.")