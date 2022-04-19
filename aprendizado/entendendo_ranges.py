'''Precisamos conhecer o loop for para usar o ranges
Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequência numéricas, não de forma aleatória, mas sim de maneira especificada.
Formas gerais:

range(valor_de_parada)
OBS: valor_de_parada não inclusive(inicio padrão 0, e passo de 1 em 1)

#Forma 1
for num in range(11): # começa com o 0 até 10
    print(num)

'''

'''
Forma 2
range(valor_de_inicio , valor_de_parada)
OBS: valor_de_parada não inclusive(inicio especificado pelo usuarios, e passo de 1 em 1)
for num in range(1,11): # começa com o 1 até 10
    print(num)
'''
'''
Forma 3
range(valor_de_inicio , valor_de_parada,passo)
OBS: valor_de_parada não inclusive(inicio especificado pelo usuarios, e passo especificado pelo usuario)
for num in range(1,10,2): # começa com o 1 até 10 contando de 2 em 2
    print(num)

for num in range(5,55,5): # começa com o 5 até 55 contando de 5 em 5
    print(num)
'''
'''
Forma 4 (Inverse)
range(valor_inicio , valor_de_parada,passo)
OBS: valor_de_parada não inclusive(valor_inicio especificado pelo usuarios, e passo especificado pelo usuario)
for num in range(10,0,-1):
    print(num)
'''
