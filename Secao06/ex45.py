'''Faca um algoritmo que converta uma velocidade expressa em km/h para m/s e vice
versa. Voce deve criar um menu com as duas opcoes de conversao e com uma op
para finalizar o programa. O usuario poder a fazer quantas conversoes desejar, sendo 
que o programa so sera finalizado quando a op de finalizar for escolhida'''




print('CONVERSOR DE VELOCIDADE'.center(40,'-'))
print('|1- KM/H para M/S '.ljust(20,' ') + '2- M/S para KM/H '.ljust(20,' ') + '|')
print('|3- FINALIZAR '.ljust(20,' ') + '|\n')
op = int(input('Qual sua Operação desejada?: '))


while op != 3:
    if op == 1:
        velo = float(input('km/h: '))
        print(f'm/s = {velo/3.6}\n')
    sair=(input('Deseja Sair?':1[Sim]ou 2[Não]))
        
    elif op == 5:
        velo = float(input('m/s: '))
        print(f'km/h = {velo*3.6}\n')
    else:
        print('Opção Invalida')
if op == 3:
    print('Obrigado e até a próxima!')
