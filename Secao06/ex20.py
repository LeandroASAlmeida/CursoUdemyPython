'''
Ler uma sequencia de numeros inteiros e determinar se eles sao pares ou nao. Dever  a
ser informado o numero de dados lidos e numero de valores pares. O processo termina 
quando for digitado o numero 1000
'''


num = int(input("Insira um número: "))
lidos = 0
pares = 0

while num != 1000: # enquanto o numero  for diferente de 1000 faça
    lidos = lidos + 1 # a Variavel lidos a cada passada pelo laço incrementa uma unidade
    if num % 2 == 0: # SE o numero for PAR
        pares = pares + 1 # o variavel pares incrementa uma unidade
        print('Esse Numero é PAR')
        num = int(input('Digite um número inteiro: '))
    elif num % 2 != 0: #ou se num for diferente de PAR , não precisa incluir a variavel 'lidos' podes ele ja foi  incluso no começo do  laço, quando foi diferente de 1000 
        print('Esse Numero é IMPAR')
        num = int(input('Digite um número inteiro: ')) # Porem não deve somar na variavel pares


print(f"dos {lidos} números lidos, {pares} são pares.")