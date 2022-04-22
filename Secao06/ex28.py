'''
Faca um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E,
conforme a formula a seguir 
E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
'''

n = int(input("Insira um valor N inteiro e positivo: "))
e = 1 # começa com 1

if n > 0:
    for x in range(1, n+1):
        f = 1 
        cont = x
        for x in range(n, 0, -1):
            while cont > 0:
                f = f * cont # vai decrementar até chegar 0
                cont -= 1
        e += 1/f# divisão por 1
else:
    print("Número invalido.")

print(e)
