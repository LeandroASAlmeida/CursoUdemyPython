'''Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
formula de conversaoe: C = K − 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.'''

k= float(input('Informe a temperatura em graus Kelvin: ')) 
c = k - 273.15 
print('A tempetura de '+ str(k) + 'graus Kelvin, convertida em Celsius é igual á ' + str(c) +'graus ' )