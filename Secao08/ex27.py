'''
27. Faca uma funcao que receba como parametro o valor de um angulo em graus e calcule 
o valor do seno desse angulo usando sua respectiva serie de Taylor:
sin x =
P∞
n=0
(−1)n
(2n+1)!x
2n+1 = x −
x
3
3! +
x
5
5! − . . . para todo x,
onde x e o valor do angulo em radianos. Considerar  π = 3.141593 e n variando de 0
ate 5. 

'''
from math import factorial


def seno(angulo):

    if angulo > 0:
        pi = 3.141593
        x = angulo * pi / 180
        sen = 0.0

        for n in range(6):
            numerador = x ** (2 * n + 1)
            denominador = factorial(2 * n + 1)
            sen += (-1) ** n / denominador * numerador

        return f"{angulo}° em radianos: {x}" \
               f"\nSeno de {x}: {sen}"

    return "Valor inválido"

if __name__ == '__main__':

    angulo = int(input("Digite o valor do ângulo em graus: "))
    print(f"\n{seno(angulo)}")

