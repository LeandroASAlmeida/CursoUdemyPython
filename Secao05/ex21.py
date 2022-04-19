'''Escreva o menu de opcoes abaixo. Leia a opcao do usuario e execute a operacao escolhida. Escreva uma mensagem de erro se a opcao for invalida.
Escolha a opcao:
1- Soma de 2 numeros.
2- Diferenca entre 2 numeros (maior pelo menor).
3- Produto entre 2 numeros.
4- Divis~ao entre 2 numeros (o denominador nao pode ser zero).
Opcao'''


opcao=float(input('Escolha a opção: \n'
                 '1-  Soma de 2 números.\n'
                 '2 - Diferença entre 2 números(maior pelo menor) \n'
                 '3 - Produto entre 2 números \n'
                 '4 - Divisão entre 2 números (o denominador não pode ser zero)\n'
                 'OPÇÂO :  '))

if opcao == 1:
    valor1=float(input('Digite um valor: '))
    valor2=float(input('Digite outro valor: '))
    soma=valor1 + valor2
    print(' A soma dos valores é {}'. format(soma))
elif opcao == 2:
    valor1=float(input('Digite um valor: '))
    valor2=float(input('Digite outro valor: '))
    if valor1 > valor2:
        dif = valor1-valor2
        print('A diferença entre o maior numero para o menor é de {}'.format(dif))
    elif valor2 > valor1:
        dif = valor2-valor1
        print('A diferença entre o maior numero para o menor é de {}'.format(dif))
    else:
        print('Não existe diferença entre os numeros')
elif opcao == 3:
    valor1=float(input('Digite um valor: '))
    valor2=float(input('Digite outro valor: '))
    prod = valor1*valor2
    print('O produto entre os valores é {}'.format(prod))
elif opcao == 4:
    valor1=float(input('Digite um valor: '))
    valor2=float(input('Digite outro valor: '))
    if valor2 == 0:
        print("O denominador não pode ser 0")
    else:
        div=valor1 / valor2
        print('A divisão entre os numeros é {}'.format(div))
else:
    print('Opção Invalida')
        



