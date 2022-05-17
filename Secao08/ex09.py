'''
9. Faca umam funcao que receba a altura e o raio de um cilindro circular e retorne o volume
do cilindro. O volume de um cilindro circular e calculado por meio da seguinte formula: 
V = π ∗ raio2 ∗ altura, onde π = 3.141592.

'''

def volume(r, a):
    return 3.141592 * (r ** 2) * a

if __name__ == '__main__': #checagem de escopo de execução

    print("Informe a altura do cilindro: ", end=" ")
    a = float(input())
    print("Informe o raio do cilindro: ", end=" ")
    r = float(input())
    print(f"Volume: {volume(r, a)}")
