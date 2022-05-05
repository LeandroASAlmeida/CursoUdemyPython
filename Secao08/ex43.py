'''
42. Faca uma funcao que receba um vetor de inteiros e o preencha com numeros aleatorios 
sem repeticao.
'''

from random import randint
import os



def num_aleat(qtd):
    valor_ale = []
    cont= 0

    while cont < qtd:
        valida=False
        while (valida == False):
            num=randint(1,9999)
            if num in valor_ale:
                pass
            else:
                valor_ale.append(num)
                valida=True
                cont+=1
    return valor_ale


os.system('cls')
qtd = int(input("Informe o tamanho da lista : "))
print(num_aleat(qtd))



  






