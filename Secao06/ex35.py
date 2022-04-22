'''Faca um programa que some os numeros impares contidos em um intervalo definido 
pelo usuario. O usuario define o valor inicial do intervalo e o valor final deste intervalo 
e o programa deve somar todos os numeros ımpares contidos neste intervalo. Caso o
usuario digite um intervalo invalido (comecando por um valor maior que o valor final) deve 
ser escrito uma mensagem de erro na tela, “Intervalo de valores invalido” e o programa 
termina. Exemplo de tela de saıda: Digite o valor inicial e valor final: 5
10
Soma dos ımpares neste intervalo: 21'''

vlr_inicial= int(input('Digite um valor inicial para o intervalo: '))
vlr_final = int(input('Digite um valor final para o intervalo: '))
soma=0

while vlr_final < vlr_inicial:
    print('Intervalo de valores invalido')
    print('FIM DO PROGRAMA')
    quit()

if vlr_final >= vlr_inicial:
    for i in range(vlr_inicial, vlr_final+1):# dentro do laço do valor inicial ao valor final
        if i % 2 != 0:# impar
            soma += i # acrescenta mais 1 na variavel i
    print('Soma dos ímpares neste intervalo: {}'.format(soma))

