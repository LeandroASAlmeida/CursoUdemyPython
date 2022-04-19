'''Faca um algoritmo que calcule o IMC de uma pessoa e mostre sua classificacao de
acordo com a tabela abaixo:'''

altura = float(input('Qual sua altura?: '))
peso = float(input("Qual seu peso em quilos? "))
imc = peso / (altura ** 2)

if imc < 18.6:
    print("Abaixo do peso.")
elif 18.6 <= imc < 25:
    print("Saudável")
elif 25 <= imc < 30:
    print("Peso em excesso")
elif 30 <= imc < 35:
    print("Obesidade Grau I")
elif 35 <= imc < 40:
    print("Obesidade Grau II (Severa)")
elif imc <= 40:
    print("Obesidade Grau III (Mórbida")