num1 = int(input('Informe um valor: '))
num2 = int(input('Informe outro valor: '))


if num1 > num2:
    dif= num1-num2
    print('O {} é o maior numero'.format(num1)+ ' e a diferença entre eles é de {}'.format(dif))
else:
    dif2 = num2-num1
    print('O {} é o maior numero'.format(num2)+ ' e a diferença entre eles é de {}'.format(dif2))