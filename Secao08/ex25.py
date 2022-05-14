'''
25. Faca uma funcao que receba um inteiro N como parametro, calcule e retorne o resultado 
da seguinte serie: 
S = 2/4 + 5/5 + 10/6 + ... + (N2 + 1)/(N + 3)

'''

def calculo(numero):

    if (numero > 0) and (numero // 1 == numero):
        resultado = 0
        for i in range(1, numero+1):
            resultado += (i ** 2 + 1) / (i + 3)

        return resultado

    elif (numero < 0) and (numero // 1 == numero):

        resultado = 0
        for i in range(numero, 1, 1):
            resultado += (i ** 2 + 1) / (i + 3)

        return resultado

    return 0

if __name__ == '__main__':

    num = int(input("Digite um número: "))
    print(f"\nResultado: {calculo(num)}")