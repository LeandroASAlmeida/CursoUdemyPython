'''
Faca um programa que receba dois numeros. Calcule e mostre:
• a soma dos numeros pares desse intervalo de numeros, incluindo os numeros digi- 
tados;
• a multiplicacao dos numeros ımpares desse intervalo, incluindo os digitados;

'''

num1 = int(input('Informe um numero : '))
num2 = int(input('Informe um segundo numero : '))

soma = 0 
multiplicacao = 1

if num1 < num2: # Se não houver diferença de intervalo entre os numero digitados, caira no else "print('Não há intervalo entre os números.'"
    for n in range(num1, num2+1):
        if n % 2 == 0:# PAR
            print(f"Número par: {n}.")
            soma = soma + n
    for n in range(num1, num2+1):
        if n % 2 != 0: # IMPAR
            print(f"Número impar: {n}.")
            multiplicacao = multiplicacao * n
elif num1 > num2:
    for n in range(num2, num1+1):
        if n % 2 == 0: # PAR
            print(f"Número par: {n}.")
            soma = soma + n
    for n in range(num2, num1+1):
        if n % 2 != 0:# IMPAR
            print(f"Número impar: {n}.")
            multiplicacao = multiplicacao * n
else:
    print('Não há intervalo entre os números.')

print('A soma entre os números pares da diferença entre os números digitados é {}.' .format(soma))
print('A multiplicação entre os números impares da diferença entre os números digitados é {}.'.format(multiplicacao))