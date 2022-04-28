'''
17. Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que
possuírem valores negativos

'''

valores=[]

for n in range(0,10):
    num =int(input('Informe 10 valores: '))
    if num < 0:
        valores.append(0)
    else:
        valores.append(num)

print(f'Numeros Zerados {valores}')


