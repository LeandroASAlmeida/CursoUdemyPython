'''
3. Faca uma funcao para verificar se um numero e positivo ou negativo.
Sendo que o valor de retorno sera 1 se positivo, -1 se negativo e 0 se for igual a 0.
'''

def positivo_negativo(numero):
    
    if numero > 0:
        return 1 
    

    elif numero < 0:
        return -1

    return 0
 
if __name__ == '__main__': #checagem de escopo de execução
    

    num = int(input("Informe um numero: "))

    print(f"\nO numero {num } é {positivo_negativo(num)}")

        