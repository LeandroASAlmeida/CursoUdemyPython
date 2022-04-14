numero = int(input('Escolha um numero : '))

if (numero % 3) == 0:
    print('O valor digitado {}, é divisel por 3'. format(numero))
else:
    print('{} não é divisivel por 3'.format(numero))
if (numero % 5) == 0:
    print('O valor digitado {}, é divisel por 5'. format(numero))
else:
    print('{}  não é divisivel por 5'.format(numero))
