'''
Faca um programa que leia 10 inteiros e imprima sua media. 
'''

num = 0
media= 0
contador = 0
num = int(input('Digite 10 numeros: [Lembre quando digitar os 10, digite 999 para encerrar] :'))
while num != 999:
    media += num /10
    contador += num
    num = int(input('Digite 10 numeros: [Lembre quando digitar os 10, digite 999 para encerrar] :'))
print(f'A média é {media}')