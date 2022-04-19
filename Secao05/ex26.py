'''Leia a distancia em  Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com
a tabela abaixo:'''


dist = float(input('Informe a distância em KM: '))
litros = float(input('Informe quantos litros consumidos: '))
consumo = dist /litros
print('O consumo do carro foi de {}'. format(consumo))

if consumo < 8:
    print('Venda o Carro')
if consumo >= 8 and consumo <= 14:
    print('Econômico!')
if consumo > 12:
    print('Super econômico')