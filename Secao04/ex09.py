'''Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
formula de conversaoe:K = C + 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.'''

c = float(input('Informe a temperatura em graus Celsius: '))
k = c + 273.15
print('A tempetura de '+ str(c) + 'graus Celsius, convertida em Kelvin é igual á ' + str(k) +'graus ' )