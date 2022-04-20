'''Faca programas para calcular as seguintes sequencias: 
1 + 2 + 3 + 4 + 5 + ... + n
1 − 2 + 3 − 4 + 5 + ... + (2n − 1)
1 + 3 + 5 + 7 + ... + (2n − 1)
'''
fator =1
c = 1
n = int(input('digite um numero:    \n'))
for c in range(n,1,-1):
       fator *=c
print('o fatorial de {} é {}'.format(n,fator))