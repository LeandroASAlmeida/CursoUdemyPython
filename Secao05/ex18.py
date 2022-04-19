'''Faca um programa que mostre ao usuario um menu com 4 opcoes de operacoes ma- 
tematicas (as basicas, por exemplo). O usuario escolhe uma das opcoes e o seu pro- 
grama entao pede dois valores numericos e realiza a operacao, mostrando o resultado e 
saindo.'''



escolha = (input("Qual operação deseja fazer?"))
valor1 = int(input("INFORME UM VALOR: "))
valor2 = int(input("INFORME OUTRO VALOR: "))



if escolha == '+':
    print('Soma: ' + str((valor1+valor2)))#soma
elif escolha == '-':
    print('Subtração: ' + str((valor1-valor2)))#subtração
elif escolha == '/':
    print('Divisão: ' + str((valor1/valor2)))#divisão
elif escolha == '*':
    print('Multiplicação: ' + str((valor1*valor2)))#multiplicação
else:
    print('Operação Invalida')