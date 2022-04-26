'''Faca um algoritmo que converta uma velocidade expressa em km/h para m/s e vice
versa. Voce deve criar um menu com as duas opcoes de conversao e com uma op
para finalizar o programa. O usuario poder a fazer quantas conversoes desejar, sendo 
que o programa so sera finalizado quando a op de finalizar for escolhida'''


while True:
    print('CONVERSOR DE VELOCIDADE'.center(40,'-'))
    print('|[1]- KM/H para M/S '.ljust(20,' ') + '[2]- M/S para KM/H '.ljust(20,' ') + '|')
    print('|[3]- FINALIZAR '.ljust(20,' ') + '|\n')
    opcao = ''
    while opcao != 1 and opcao != 2 and opcao != 3:
        opcao = int(input('Insira a opção desejada: '))

    if opcao == 1:
        velo = float(input('km/h: '))
        print(f'm/s = {velo/3.6}\n')
    elif opcao == 2:
        velo = float(input('m/s: '))
        print(f'km/h = {velo*3.6}\n')
    else:
        print('PROGRAMA ENCERRADO!')
        break

