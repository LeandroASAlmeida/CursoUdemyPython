'''Faca um programa que calcule e mostre a soma dos 50 primeiros numeros pares'''

num = int(input("Digite o numero 0: "))
while num != 0:
    print('Por favor , digita só o "0"')
    num = int(input("Digite o numero 0: "))
if num == 0:
    for n in range(0, 101):
        if n % 2 == 0: # descobrir se é par e a divisão é igual a 0
            num = num + n 
            print(n)
print('A soma dos 50 numeros pares é {}'. format(num))



