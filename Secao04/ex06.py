''' Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A formula de conversaoe: F = C∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.'''

c =float(input('Informe a temperatura em graus Celsius: '))

f = c*(9.0/5.0)+32.0 
print('A tempetura de '+ str(c) + 'graus Celsius, convertida em Fahrenheit é igual á ' + str(f) +'graus ' )