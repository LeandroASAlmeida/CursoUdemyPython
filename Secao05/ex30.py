'''Faca um programa que receba tres numeros e mostre-os em ordem crescente'''

num1= int(input('Informe um numero : '))
num2= int(input('Informe outro numero : '))
num3= int(input('Informe o ultimo numero : '))

if num1 <= num2 and num1 <= num3 and num2 <= num3:
    print(f'A ordem crescente é {num1} - {num2} - {num3}')
elif num1 <= num2 and num1 <=num3 and num3 <= num2:
    print(f'A ordem crescente é {num1} - {num3} - {num2}')
elif num2 <= num1 and num2 <= num3 and num1 <= num3:
    print(f'A ordem crescente é {num2} - {num1} - {num3}')
elif num2 <= num1 and num2 <= num3 and num3 <= num1:
    print(f'A ordem crescente é {num2} - {num3} - {num1}')
elif num3 <= num1 and num3 <= num2 and num1 <=num2:
    print(f'A ordem crescente é {num3} - {num1} - {num2}')
elif num3 <= num1 and num3 <= num2 and num2 <= num1:
    print(f'A ordem crescente é {num3} - {num2} - {num1}')