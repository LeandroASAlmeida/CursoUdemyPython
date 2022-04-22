'''Faca programas para calcular as seguintes sequencias: 
1 + 2 + 3 + 4 + 5 + ... + n
1 − 2 + 3 − 4 + 5 + ... + (2n − 1)
1 + 3 + 5 + 7 + ... + (2n − 1)
'''

n = int(input('Insira um número inteiro e positivo: '))
soma1 = 0
soma2 = 0
soma3 = 0

if n > 0:
    #  sequencia 1:
    for i in range(n+1):
        soma1 += i
    for i in range(2 * n):
        if i % 2 == 0:
            soma2 -= i       # verificar se o proxima será somar ou subtrair
        else:
            soma2 += i
    for i in range(2 * n):
        if i % 2 != 0:
            soma3 += i
else:
    print('Número inválido.')

print('O resultado da primeira sequencia é {}'.format(soma1))
print('O resultado da segunda sequencia é {}'.format(soma2))
print('O resultado da terceira sequencia é {}'.format(soma3))

