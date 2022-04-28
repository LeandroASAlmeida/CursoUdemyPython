'''
3. Ler um conjunto de números reais, armazenando-os num vetor e calcular o
quadrado das componentes deste vetor, armazenando o resultado noutro vetor. Os
conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.

'''

valores = []
calculo_quadrado = []

for n in range(0,10):
    num =float(input('Informe 10 valores reais: '))
    valores.append(num)

for elemento in valores:
    elementoaoquadrado = elemento ** 2
calculo_quadrado.append(elementoaoquadrado)

print(f"Lista: {valores}.")
print(f"Lista elevada ao quadrado: {calculo_quadrado}.")