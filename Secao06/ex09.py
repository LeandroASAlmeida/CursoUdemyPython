'''Faca um programa que leia um numero inteiro N e depois imprima os N primeiros
numeros naturais ımpares'''



n = int(input("Digite o valor de n: ")) 
i = 0  # contador de ímpares impressos 
ímpar = 1  # primeiro número ímpar

    # imprima os n primeiros impares, um por linha
while i < n:  
       print(ímpar) # imprima o próximo número ímpar
       i = i + 1  # incremente o contador
       ímpar = ímpar + 2 # determine o próximo ímpar