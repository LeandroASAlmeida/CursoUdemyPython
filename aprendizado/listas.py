'''Listas
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
'''

lista1 = [1,2,3,8,66,1,32,336,23,22] #inteiros
lista2 = ['l','e','a','n','d','r','o']#strings
lista3 = []
lista4 = list(range(11))#range =gera numero
print(lista4)
lista5 = list('Geek University')
nova =[1,2,3]
