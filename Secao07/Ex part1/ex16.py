'''
16. Faça um programa que leia um valores de 5 posições para números reais e, depois,
um código inteiro. Se o código for zero, finalize o programa; se for 1, mostre o valores na
ordem direta; se for 2, mostre o valores na ordem inversa. Caso, o código for diferente
de 1 e 2 escreva uma mensagem informando que o código é inválido.

'''

valores=[]
codigo= -1

for n in range(0,5):
    num =float(input('Informe 5 valores reais: '))
    valores.append(num)

print('\nEscolha uma das opções abaixo:'
      '\n[0] Finalizar o programa'
      '\n[1] Imprimir o vetor'
      '\n[2] Imprimir o vetor na forma inversa')

while codigo not in (0, 1, 2):
    print('Codigo Inválido')
    codigo = int(input('Digite 0, 1 ou 2: '))

    if codigo == 0:
        print('Fim do programa.')
    elif codigo == 1:
        print(f'\nVetor: \n{valores}')
    elif codigo == 2:
        print(f'\nVetor invertido: \n{valores[::-1]}')

 