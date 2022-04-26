'''
Faca um programa que conte quantos numeros primos existem entre a e b, onde a e b
sao numeros informados pelo usuario

'''
num1 = int(input('Informe um numero: '))
num2 = int(input('informe outro numero: '))
quant_primos = 0

for i in range(num1, num2+1):
    divide = 0
    for j in range(1, i+1):
        if i % j == 0:
            divide += 1

        if divide > 2:
            break

    if divide == 2:
        quant_primos += 1

print(f'Total de números primos no intervalo {num1} á {num2}: ')
print(quant_primos)
