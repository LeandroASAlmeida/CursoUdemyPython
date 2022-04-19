'''Escreva um programa que leia um numero inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algarismos. Por exemplo, ao numero 251 corresponder a o valor
8 (2 + 5 + 1). Se o numero lido nao for maior do que zero, o programa terminar a com a 
mensagem “Numero invalido”.'''

num = int(input('Informe um valor com no minimo 2 digitos: '))

if num < 10:
    print('Numero impossivel de efetuar soma')
else:
   A = int(num // 1 % 10)

   B = int(num // 10 % 10)      # fazer a separação dos digitos, nesse caso em até 4 digitos e transformar cada um em uma variavel.

   C = int(num // 100 % 10)

   D = int(num // 1000 % 10)

   soma = A + B + C + D

   print(f'A soma dos algorismo é {soma}') # outra forma de chamar a variavel  dentro do texto.
