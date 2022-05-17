'''
18. Faca uma funcao que receba por parametro dois valores  X e Z. Calcule e retorne o
resultado de XZ para o programa principal. Atencao! nao utilize nenhuma funcao pronta 
de exponenciacao.

'''

def potencia(x, z):
    return x ** z

if __name__ == '__main__': #checagem de escopo de execução

    print("Informe um numero: ", end=" ")
    x1 = int(input())
    print("Informe outro numero para ser a exponenciação: ", end=" ")
    z1 = int(input())
    print(f"Resultado: {potencia(x1,z1)}")

