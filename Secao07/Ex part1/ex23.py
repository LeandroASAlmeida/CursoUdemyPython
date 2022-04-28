'''
23. Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o
produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois
conjuntos e o produto escalar, sendo que o produto escalar é dado por: x1 * y1 + x2 *
y2 + ::: + xn * yn.
'''
x=[]
y=[]
prod_esc = 0

for n in range(0,5):
    num =float(input(f'X[{n}]: '))
    x.append(num)

for i in range(0,5):
    num2 =float(input(f'Y[{i}]: '))
    y.append(num2)

prod_esc += x[n] * y[i]

print(x)
print(y)
print(f'Produto escalar entre X e Y: {prod_esc}')
