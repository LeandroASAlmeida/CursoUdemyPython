ano = int(input('Informe um ano: '))

if ano % 400 == 0 or  ano % 4 == 0 or ano % 100 != 0:
    print('O ano digitado é bisexto')
else:
    print(' O ano digitado não é bisexto')




