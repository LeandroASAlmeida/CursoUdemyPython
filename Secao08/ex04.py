'''
4. Faca uma funcao para verificar se um numero e um quadrado perfeito. Um quadrado 
perfeito e um numero inteiro no negativo que pode ser expresso como o quadrado de 
outro numero inteiro. Ex: 1, 4, 9...

'''

def quadrado_perfeito(numero):
    
    if numero > 0:

        # quadrado do número digitado é um inteiro
        if (numero ** 0.5) // 1 == numero ** 0.5:
            print("\nQuadrado perfeito")

        else:
            print("\nNão é um quadrado perfeito")

    else:
        print("\nO número deve ser positivo")


if __name__ == '__main__': #checagem de escopo de execução

    num= int(input("Digite um numero: "))

    quadrado_perfeito(num)
