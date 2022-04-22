'''
. Faca um programa que calcula a associacao em paralelo de dois resistores  R1 e R2
fornecidos pelo usuario via teclado. O programa fica pedindo estes valores e calculando 
ate que o usuario entre com um valor para resistencia igual a zero. 
R =
R1 ∗ R2
R1 + R2
'''

r=0
r1 = float(input('Informe o primeiro resistor :   '))
r2 = float(input('Informe o segundo resistor :   '))


while True:
    r = (r1 * r2) / r1 + r2
    print(f"A associação é {r}.")
    r1 = int(input("Digite um valor R1: "))
    if r1 == 0:
        print('Digitado "0" e o programa sera encerrado')
        break
    r2 = int(input("Digite um valor R2: "))
    if r2 == 0:
        print('Digitado "0" e o programa sera encerrado')
        break




