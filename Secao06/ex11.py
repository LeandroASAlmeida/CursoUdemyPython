'''Faca um programa que leia um numero inteiro positivo  N e imprima todos os numeros 
naturais de 0 ate N em ordem crescente'''



n = int(input("Digite um valor positivo : ")) 
i = 0  # contador


while n < 0:
    print('Favor digitar só numeros positivos')
    n = int(input("Digite um valor positivo de n: "))
if n > 0: # se o numero digitado for maior que 0
    for i in range(n + 1): # pegue o contador e incremente +1 até chegar no "n" digitado.
        print(i) 
      
