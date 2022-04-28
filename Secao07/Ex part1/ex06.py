'''6. Faça um programa que receba do utilizador um vetor com 10 posições. Em seguida
deverá ser impresso o maior e o menor elemento do vetor.'''


valores=[]

for n in range(0,10):
    num =int(input('Informe 10 valores inteiros: '))
    valores.append(num)
print(valores)

print('O Maior valor digitado foi:')
print(max(valores))

print(f'O Menor valor digitado foi:') 
print(min(valores))

