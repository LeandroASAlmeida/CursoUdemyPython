'''
Faca um programa que apresente um menu de opcoes para o calculo das seguintes 
operacoes entre dois numeros: 
• adicao (opcao 1) 
• subtracao (opcao 2) 
• multiplicacao (opcao 3) 
• divisao (opcao 4). 
• saıda (opcao 5) 

O programa deve possibilitar ao usuario a escolha da operacao desejada, a exibicao do 
resultado e a volta ao menu de opcoes. O programa so termina quando for escolhida a 
opcao de saıda (opcao 5).

'''

while True:
    print('CALCULADORA'.center(40,'-'))
    print('|1- ADIÇÃO'.ljust(20,' ') + '2- SUBTRAÇÃO '.ljust(20,' ') + '|')
    print('|3- MULTIPLICAÇÃO '.ljust(20,' ') + '4- DIVISÃO '.ljust(20,) +'|')
    print('|5- SAIDA '.ljust(20,' ') + '\n')
    op =''

    while op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
        op = int(input('Insira a opção desejada: '))

    if op == 1:
        num1 = int(input('informe um numero: '))
        num2 = int(input('Informe outro numero: '))
        result = num1 + num2
        print('O Resultado da Adição é: {}\n'.format(result))

    elif op == 2:
        num1 = int(input('informe um numero: '))
        num2 = int(input('Informe outro numero: '))
        result = num1 - num2
        print('O Resultado da Subtração é: {}\n'.format(result))

    elif op == 3:
        num1 = int(input('informe um numero: '))
        num2 = int(input('Informe outro numero: '))
        result = num1 * num2
        print('O Resultado da Multiplicação é: {}\n'.format(result))

    elif op == 4:
        num1 = int(input('informe um numero:  '))
        num2 = int(input('Informe outro numero: '))
        result = num1 / num2
        print('O Resultado da Divisão é: {}\n'.format(result))

    else:
        print('PROGRAMA ENCERRADO!')
        break
    
