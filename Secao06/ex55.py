'''
Escreva um programa que leia um inteiro nao negativo n e imprima a soma dos n primeiros numeros primos.
'''

n = int(input('Digite um número inteiro positivo: '))
soma = 0
conta = 0
num = 2 # inicia com o primeiro numero primo(que é PAR)

while conta < n:#Enquanto a conta for menor que o numero digitado
    primo = True
    for i in range(2, num): 
        if num % i == 0: # Se for PAR ,, primo vira False
           primo = False
           break
    if primo:
        print(num)
        soma += num
        conta += 1
    num += 1
print('O Resultado da Soma é {}'.format(soma))