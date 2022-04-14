a = float(input('Informe um lado do triângulo: '))
b = float(input('Informe um lado do triângulo: '))
c = float(input('Informe um lado do triângulo: '))

if ((a == 0) and (b == 0) and (c == 0)):
    print('Os lados informados não formam um triângulo')
elif ((a == b) and (a == c)):
    print('Triângulo equilatero, possui os três lados iguais')
elif ((a == b) or (a == c) or (b == c)):
    print('Triângulo Isosceles, possui o comprimento de dois lados iguais')
elif ((a != b) and (a != c) and (b != c)):
    print('Triângulo escaleno, possui os três lados diferentes')



           