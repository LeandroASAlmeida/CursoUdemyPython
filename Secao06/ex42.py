'''
Faca um programa que leia um conjunto nao determinado de valores, um de cada vez, e 
escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize
a entrada de dados com um valor negativo ou zero.
'''

valor= int(input("Digite um valor : "))

while valor > 0:
    print(f"Ao quadrado: {valor ** 2}")#quadradoo 
    print(f"Ao cubo: {valor ** 3}")#cubo
    print(f"Raiz quadrada: {valor **(1/2)}") #raiz quadrada
    valor = int(input("Insira um número: "))
if valor <= 0:
    print('Digitado "0" ou um valor negativo.')
    print('Fim do programa')

