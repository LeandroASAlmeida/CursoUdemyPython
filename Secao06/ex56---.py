'''
.Faca um programa que calcule a soma de todos os numeros primos abaixo de dois 
milhoes
'''
n = 2# inicia com o primeiro numero primo(que é PAR)
soma = 0
conta = 0
num = 2_000_000 

while conta < num:#Enquanto a conta for menor que o numero digitado
    primo = True
    for i in range(2, num): 
        if num % i == 0: # Se for PAR ,, primo vira False
           primo = False
           break
    if primo:
        soma += num
        conta += 1
    num += 1
print('O Resultado da Soma é {}'.format(soma))




