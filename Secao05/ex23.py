'''Determine se um determinado ano lido e bissexto. Sendo que um ano e bissexto se 
for divisıvel por 400 ou se for divisıvel por 4 e nao for divisıvel por 100. Por exemplo:
1988, 1992, 1996'''


ano = int(input('Informe um ano: '))

if ano % 400 == 0 or  ano % 4 == 0 or ano % 100 != 0:
    print('O ano digitado é bisexto')
else:
    print(' O ano digitado não é bisexto')




