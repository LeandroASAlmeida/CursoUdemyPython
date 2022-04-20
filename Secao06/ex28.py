'''
Faca um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E,
conforme a formula a seguir 
E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
'''



n = int(input("Insira um valor N inteiro e positivo: "))
e = 1

if n > 0 or n != 0:
    for x in range(1, n+1):
        e = 1 
        cont = x
        for x in range(n, 0, -1):
            while cont > 0:
                e = e * cont
                cont -= 1
        e += 1/e
elif n == 0:
        print('Resultado de 0 = 1')
else:
    print("Número invalido.")

print('O valor N digitado foi {} e a o Resultado de E é {:.0f}.'.format(n,e))