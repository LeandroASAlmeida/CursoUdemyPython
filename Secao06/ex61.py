'''
Faca um programa que calcule o maior numero palındromo feito a partir do produto de
dois numeros de 3 dıgitos. Ex: O maior palındromo feito a partir do produto de dois
numeros de dois dıgitos e 9009 = 91*99.

'''

maior = 0
for i in range(100, 1000):# limite de numeros com 3 digitos
    for n in range(100, 1000):
        frente = str(i*n)
        tras = (str(i*n)[::-1]) #reverso
        if frente == tras:
            if maior < i * n:
                maior = i * n

print(maior)

