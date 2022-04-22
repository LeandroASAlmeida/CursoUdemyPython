'''
Faca um programa que calcule a area de um triangulo, cuja base e altura sao fornecidas 
pelo usuario. Esse programa nao pode permitir a entrada de dados invalidos, ou seja, 
medidas menores ou iguais a 0.
'''


base =float(input('informe o valor da base do triângulo: '))
alt = float(input('informe a altura do triângulo: '))
area= 0

while base <=0 or alt <=0:
    print('Dados invalidos')
    base =float(input('informe o valor da base do triângulo: '))
    alt = float(input('informe a altura do triângulo: ')) 

if base > 0 and alt > 0 :
    area= (base**2 + alt**2) / 2

print('A = {}'. format(area))





