'''
34. Faca uma funcao 'nao-recursiva' que receba um 'numero inteiro positivo impar' N e retorne 
o fatorial duplo desse numero. O fatorial duplo  e definido como o produto de todos os 
numeros naturais ımpares de 1 ate algum numero natural ımpar N. Assim, o fatorial duplo
de 5 e:´ 5!! = 1 * 3 * 5 = 15

'''

def fatorial_duplo(n):
    soma=1 #naturais ımpares de 1 ate algum numero natural ımpar
    for i in range(1, n + 1,2):
        soma *= i
    return soma

if __name__ == '__main__':

    print("Informe um numero inteiro e positivo: ", end=" ")
    num = int(input())
    print(f"Fatorial duplo: {fatorial_duplo(num)}", end=" ")

