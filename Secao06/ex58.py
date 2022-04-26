'''
. Faca um programa que some os numeros primos existentes entre  a e b, onde a e b sao
numeros informados pelo usuario.

'''

num1 = int(input('Informe um numero: '))
num2 = int(input('informe outro numero: '))
soma_primos = 0


for i in range(num1, num2+1):
    divide = 0
    for j in range(1, i+1):
        if i % j == 0:
            divide += 1

        if divide > 2:
            break

    if divide == 2:
        soma_primos += i

print('A soma é {}'. format(soma_primos))




