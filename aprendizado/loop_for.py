'''
loop é uma estrutura de repetição
for é uma dessas estruturas
for = para

C ou java
for(int=0; i < limitador; i++){
    //instrução qualquer
}


Python

for item in interavel:
    //instrução qualquer

Utilizamos loops para iterar sobre sequência ou sobre valores iteráveis

exemplos de iteraveis:
-string
    nome = 'Geek University'
-Lista
    lista = [1,3,5,7,9]
-Range
    numeros = range(1,10)

'''

'''/*Exemplo de for 1 (Iterando em uma string)
nome = 'Geek University'
lista = [1,3,5,7,9]
numeros = range(1,10) # Temos que transformar em uma lista

for indice,letra in enumerate(nome):
    print(nome)

for indice,letra in enumerate(nome):
    print(letra)

for _,letra in enumerate(nome):# quando não precisamos de um valor, podemos descarta-lo usando o (_)
    print(letra)

for valor in enumerate(nome):
    print(valor)'''


'''string
for letra in nome:
    print (letra)

Exemplo de for 2 (Iterando em uma lista)
for numero in lista:
    print(numero)

Exemplo de for 3 (Iterando sobre um range)
range (valor_inicial , valor_final)
OBS: O valor final não é inclusive

1
2
3
4
5
6
7
8
9
10- não inclui



for numero in range(1,10):
    print(numero)'''

'''qtd = int(input('Quantas vezes esse loop deve rodar? :'))
soma= 0
for n in range(1, qtd+1):
    #print(f'Imprimindo:{n}')
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma +num
print(f'A Soma é {soma}')'''

'''nome= 'Geek University'
for letra in nome:   
    print(letra)  # IMPRIMI UMA LETRA ABAIXO DA OUTRA

    nome= 'Geek University'
for letra in nome:   
    print(letra, end='')  # IMPRIMI UMA LETRA AO LADO DA OUTRA'''


'''#Concatenação de string
nome = 'Geek'
concatenar = nome + ' University'
print(concatenar)'''

#tabela de emojis unicode : https://apps.timwhitlock.info/emoji/tables/unicode

#Original : U+1F635
#modificado: U0001F635

nome ='Geek '
emoji= 'U0001F635'
for num in range(1,11):
    print('\U0001F635' * num)

for _ in range(3):
    for num in  range(1,11):
        print('\U0001F635' * num)