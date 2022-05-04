'''
15. Crie um programa que receba tres valores (obrigatoriamente maiores que zero), repre-
sentando as medidas dos tres lados de um triangulo. Elabore funcoes para: 
(a) Determinar se eles lados formam um triangulo, sabendo que: 
• O comprimento de cada lado de um triangulo  e menor do que a soma dos outros 
dois lados.
(b) Determinar e mostrar o tipo de triangulo, caso as medidas formem um triangulo. 
Sendo que:
• Chama-se equilatero o triangulo que tem tres lados iguais. 
• Denominam-se isosceles o triangulo que tem o comprimento de dois lados 
iguais.
• Recebe o nome de escaleno o triangulo que tem os tres lados diferentes.

'''

def triangulo(med1,med2,med3):
    if med1 - med2 < med3 < med2 + med1:
        if med1 == med2 == med3:
            return 'Equilátero'
        
        elif med1 == med2 or med3 == med1:
            return 'Isósceles'
        else:
            return 'Escaleno'
    return "triangulo invalido."

print("Informe a primeira medida: ", end=" ")
m1 = float(input())
print("Informe a segunda medida: ", end=" ")
m2 = float(input())
print("Informe a terceira medida: ", end=" ")
m3 = float(input())
print(f"\n Triangulo {m1} , {m2} , {m3} é  {triangulo(m1,m2,m3)}")