'''
Faca um programa que simula o lancamento de dois dados, d1 e d2, n vezes, e tem como
saıda o numero de cada dado e a relacao entre eles (>,<,=) de cada lancamento.
'''


v = int(input('Quantas comparações serão feitas? '))
for n in range(v):
    d1 = int(input('Digite o primeiro valor: '))
    d2 = int(input('Digite o segundo valor: '))
    if d1 == d2:
        print(f'{d1} = {d2}')
    elif d1 < d2:
        print(f'{d1} < {d2}')
    else:
        print(f'{d1} > {d2}')