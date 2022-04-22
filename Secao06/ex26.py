'''
Faca um algoritmo que encontre o primeiro multiplo de 11, 13 ou 17 apos um numero 
dado
'''

'''num=int(input('Digite o numero: '))'''


num = int(input('Digite um número inteiro: '))

while True: # quando achar o primeiro resultado. imprima
    num += 1
    if (num % 11 == 0) or (num % 13 == 0) or (num % 17 == 0):
        print(num)
        break














