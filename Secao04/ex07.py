'''Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A formula de conversaoe: C = 5.0 ∗ (F − 32.0)/9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit.'''


f = float(input('Informe a temperatura em graus Fahrenheit: '))
c = 5.0 *(f-32.0)/9.0
print('A tempetura de '+ str(f) + 'graus Fahrenheit, convertida em Celsius é igual á ' + str(c) +'graus ' )