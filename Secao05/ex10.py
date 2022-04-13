h = float(input('Informe sua altura: '))
sexo = input('Informe seu sexo:[M] ou [F]: ')


if (sexo == 'M'):
    pesoideal=(72.7 * h)- 58
    print('O peso ideal para você homem é de {}'. format(pesoideal))
elif (sexo == 'F'):
    pesoideal=(62.1* h)- 44.7
    print(' O peso ideal para você mulher é de {}'.format(pesoideal))
