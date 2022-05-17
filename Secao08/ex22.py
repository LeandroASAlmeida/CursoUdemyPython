'''
22. Crie uma funcao que receba como parametro um valor inteiro e gere como saıda n linhas
com pontos de exclamacao, conforme o exemplo abaixo (para n = 5): 
!
!!
!!!
!!!!
!!!!!
'''

def vlr_int(num):
    lista = list()
    for i in range(num+1):
        lista.append("!"*i)
    return lista

if __name__ == '__main__': #checagem de escopo de execução

    print("Informe um numero inteiro: ", end=" ")
    num = int(input())
    for item in vlr_int(num):
        print(item)
