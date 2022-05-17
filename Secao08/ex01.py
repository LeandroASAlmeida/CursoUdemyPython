'''
1. Crie uma funcao que recebe como parametro um numero inteiro e devolve o seu dobro.
'''
def inteiro(num):
    num = num * 2
    return num
 

if __name__ == '__main__':
    
    int = int(input('Informe um numero inteiro: '))
    print(f' O dobro de {int} é {inteiro(int)}')