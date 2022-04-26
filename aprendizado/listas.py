'''Listas ( list ) 
 funcionam como  vetores , matrizes ou arrays. com a diferença de serem DINÂMICOS  e tambem de podermos colocar QUALQUER tipo de dado.

-C ou Java=
Possuem tamanho e tipo de dado fixo
Ou seja, nestas linguagens se você criar um array do tipo inteiro com tamanho 5 sera sempre do tipo int e podera ter sempre no maximo 5 valores

-Python = 
Dinâmico: não possuem tamanho fixo, ou seja podemos criar a lista e simplesmente adicionando elemento;
Qualquer tipo de dado: Não possuem tipo de dado fixo: OU seja, podemos colocar qualquer tipo de dado: 

LISTA  É REPRESENTADA POR  "[]"
'''

'''#ltype([])

print(lista5)'''

'''#Exemplo:
#Podemos facilmente checar se determinado valor está contido na lista

num = 7

lista4 = list(range(11))

if num in lista4:
    print(f'Encontrei o {num}')
else:
    print(f'Não encontrei o {num}')


lista5 = list('Geek University')

if 'e' in lista5:
    print('Encontrei a letra e' )
else:
    print('Não encontrei a letra e')


lista5 = list('Geek University')'''

'''#Podemos facilmente ordernar uma lista

lista1.sort()
print(lista1)'''

'''#Podemos facilmente contar o nuemro de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))'''

'''#Adicionando elementos em uma lista, ultizamosa função append( SOMENTE UM ELEMENTO POR VEZ )
print(lista1)
lista1.append(42) # adiciona no fim da lista
print(lista1)'''

'''lista1.append([8,2,3]) # coloca a lista como elemento unico- SEMPRE NO FINAL
print(lista1)'''

'''if [8,2,3] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')'''

'''lista1.extend([123,44,67]) # coloca cada elemento da lista como valor adicional a lista - SEMPRE NO FINAL
print(lista1)'''

'''lista1.extend('Geek') # coloca cada elemento da lista como valor adicional a lista, (inteiro + string)
print(lista1)'''


'''Podemos inserir um novo elemento na lista informando a posição do indice
#isso não substitui o valor inicial.o mesmo será deslocado para frente
lista1.insert(2,'Novo Valor')
print(lista1)'''

'''#lista6 = lista1+lista2
lista1.extend(lista2)
print(lista1)'''


'''podemos imprimir a lista ao contrario
lista1.reverse()
lista5.reverse()
print(lista1)
print(lista5)'''

'''print(lista5[::-1])
print(lista1[::-1])'''

'''>copiar Lista

lista6 = lista2.copy()
#imprimir o tamanho de uma lista
print(len(lista1))
print(len(lista2))
print(len(lista3))
print(len(lista4))
print(len(lista5))
'''

'''#Podemos remover facilmente o ultimo elemento de uma lista
#obs= o pop remove o ultimo elemento mas tmb o retorna

print(lista5)
lista5.pop()
print(lista5)'''

'''#Podemo remover um elemento pelo indice
#obs: os elementos a direta desse indice serão deslocado para a esquerda
#Se não houver elementono indice informado, teremos o erro IndexError
lista5.pop(2)
print(lista5)


#Podemos zera a lista

print(lista5)
lista5.clear()
print(lista5)

#podemos repetir  elementos em uma lista
nova =[1,2,3]
print(nova)
nova = nova * 3
print(nova)
print(lista6)'''

'''#Podemos favilment converter uma string em uma lista
#Split =  separa os elementos da lista pelo espaço entre eles
curso =' Python basico ao avançado'
print(curso)
curso= curso.split()
print(curso)

#Exemplo2

curso ='Programação,em,Python,essencial'
print(curso)
curso=curso.split(',') #escolher qual vai ser o tipo de separador
print(curso)

#Convertendo uma lista em uma string
print(lista6)

#Abaixo estamos falando : Pega a lista 6 e coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso) 

#Abaixo estamos falando : Pega a lista 6 e coloca o $ entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Iterando sobre listas


#ultilizando FOR
soma = 0
for elemento in lista1:
    print(elemento)
    soma =soma + elemento
print(soma)

#ultilizando WHILE

carrinho = []
produto = ''
while produto != ' sair':
    print('Adiciona um produto na lista ou digite sair para encerrar: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

#ultilizando variáveis em listas

numero = [1,2,3,4,5]

num1=1
num2=2
num3=3
num4=4
num5=5

numeros = [num1,num2,num3,num4,num5]

# Fazemos acesso aos elemtos de forma indexada

cores = ['verde','amarelo','azul','branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

#Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o indice negativo, pense na lista como um circulo, onde o final de um elemento esta ligado ao inicio dea lista

print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

# for  and while com as cores:

for cor in cores:
    print(cores)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1


# Gerar indice em um for

for indice , cor in enumerate(cores): #para as novas variaveis incdice e cor, quero que enumere cada cor 
    print(indice,cor) # imprima indice e cor, cada cor com seu numero.


# listas a aceitam valores repetidos

lista = []
lista.append(42)
lista.append(10)
lista.append(11)
lista.append(42)
lista.append(66)
lista.append(84)

print(lista)


#Outros metodos não tão importantes mas tambem uteis

#Encontre o indice de um elemento na lista

numeros = [2,6,9,4,6,22,33,14,25,10,15,13]
#Em qual indice da lista esta o valor 6?
print(numeros.index(6))

#Em qual indice da lista esta o valor 6?
print(numeros.index(9))

#OBS: Caso não tenha esse elemneto na lista sera apresentado erro
#print(numeros.index(5))

# Retorna o indice do primeiro encontrado , se tiver repetição
print(numeros.index(6))

#Podemos fazer uma busca dentro de um range, ou seja, qual indice começa a buscar
print(numeros.index(6,2))#busque a partir do indice 2, onde ele vai encontrar o 6 repetido
print(numeros.index(6,3))#busque a partir do indice 3, onde ele vai encontrar o 6 repetido
#OBS: Caso não tenha esse elemneto na lista sera apresentado erro ValueErro

#Podemo fazer buscas dentro de um range

print(numeros.index(6,2,11))# buscar o indice de valor , entre 2 a 11(LEMBRANDO QUE O 6 É O NUMERO QUE DESEJO ENCONTRAR NO MEIO DA LISTA)


#REVISANDO SLICING

#lista[incio:fim:passo]
#range[incio:fim:passo]

#Trabalhando com slice de lsita com o parametro inicio

lista = [1,2,3,4,5,]
print(lista[1::]) #Iniciandono indice 1 e pegando todos os elementos restantes, ele vai ignorar o elemento 0 e printar [2,3,4,5]


#Trabalhando com slice de lista com o parametro fim

lista = [1,2,3,4,5,]
print(lista[:2:]) #Pelo indice final 2 e pegando todos os elementos restantes anteriores, ele vai ignorar o elemento 3 e printar [1,2]
print(lista[:4:]) #Pelo indice final 4 e pegando todos os elementos restantes anteriores, ele vai ignorar o elemento 5 e printar [1,2,3,4]

print(lista[1:3:]) #Pelo indice inicial 1 e até o final 3 e pegando todos os elementos dentro desse intervalo, ele printar [2,3]

#Trabalhando com slice de lista com o parametro passo

print(lista[1::2]) # começa em 1 , vai até o final , e print de 2 em 2

print(lista[::2]) # começa em 0 , vai até o final , e print de 2 em 2

print(lista[0::]) # começa em 0 , vai até o final ( SOMENTE MOSTRA A LISTA)
print(lista[::-1]) # começa em 0 , vai até o final , e passo de -1  (Inverte a lista)



#Invertendo valores em uma lista

nomes =['Geek','University']
nomes[0],nomes[1] = nomes[1],nomes[0] # troca de posição as palavras a saida será  ['University', 'Geek']
print(nomes)  # OU MESMA COISA QUE 

nomes =['Geek','University']
nomes.reverse()
print(nomes)



#Soma*, Valor Maximo*, Valor Minimo* ,Tamanho
#* = Se os valores forem todos inteiros ou reais

lista =[1,2,3,4,5,6]
print(sum(lista)) # soma da lista toda
print(max(lista)) # o valor maximo da lista
print(min(lista)) # o valor minimo da lista
print(len(lista)) # o tamanho da lista


# Tranformando Lista em Tupla

lista =[1,2,3,4,5,6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

#Desempacotamento de listas

lista =[1,2,3,4] # OBS : Se tivermos mais elementos para desempacotar do que variaveis para receber  os valores, teremos  ValueError
              
num1,num2,num3 = lista
                 # OBS : Se tivermos mais variaveis para declarar do que elementos para vincular a lista , teremos  ValueError

print(num1)
print(num2)
print(num3)



#Copia de lista para outra(Shallow Copy e Deep Copy)

lista =[1,2,3,4]
print(lista)

nova = lista.copy() # copia
print(nova)

nova.append(5)
print(nova)

#Ao Ultilizar a lista.copy() , copiamos od dados  para uma nova lista, mas ficaram totalmentes independentes
#ambas existem
#isso se Chama DEEP COPY


lista = [1,2,3,4]
print(lista)

nova = lista # copia
print(nova)

nova.append(5)
print(nova)
print(lista)

#Veja que ultilizamos a cópia via atribuição e copiamos dados da lista para a nova lista., mas apos realizar modificações em uma das listas, ambas foram alteradas.
'''

lista1 = [1,2,3,8,66,1,32,336,23,22] #inteiros
lista2 = ['l','e','a','n','d','r','o']#strings
lista3 = []
lista4 = list(range(11))#range =gera numero
print(lista4)
lista5 = list('Geek University')
nova =[1,2,3]
lista6= ['Programação','em','Python','Essencial']
lista7 = [1,2,34, True,'Geek','d',[1,2,3], 45345345345]
print(lista7)
print(type(lista6))
cores = ['verde','amarelo','azul','branco']
