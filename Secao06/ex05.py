'''Faca um programa que peca ao usuario para digitar 10 valores e some-os'''

num = 0
soma= 0
contador = 0
num = int(input('Digite 10 numeros: [Lembre quando digitar os 10, digite 999 para encerrar] :'))
while num != 999:
    soma += num
    contador += num
    num = int(input('Digite 10 numeros: [Lembre quando digitar os 10, digite 999 para encerrar] :'))
print(f'A Soma é {soma}')






