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
