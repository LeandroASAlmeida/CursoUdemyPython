'''Escreva um programa para calcular o valor da serie, para 5 termos. 
S = 0 + 1/2! + 2/4! + 3/6! + ...'''


n = int(input("Insira um valor N inteiro e positivo: "))
s = 0

if n > 0 or n != 0:
    for cont in range(1,6 ):
        while cont > 0:
            cont += 1
elif n == 0:
        print('Resultado de 0 = 1')
else:
    print("Número invalido.")

print('O valor digitado foi {} e a o Resultado de S em 5 termos é {:.0f}.'.format(n,s))

