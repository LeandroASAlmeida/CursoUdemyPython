'''
28. Faca uma funcao que receba como par ametro o valor de um angulo em graus e calcule 
o valor do cosseno desse angulo usando sua respectiva serie de Taylor: 
cos x =
P∞
n=0
(−1)n
(2n)! x
2n = 1 −
x
2
2! +
x
4
4! − . . . para todo x,
onde x e o valor do angulo em radianos. Considerar π = 3.141593 e n variando de 0
ate 5.

'''


from math import factorial

def cosseno(angulo):

    if angulo > 0:
        pi = 3.141593
        x = angulo * pi / 180
        cos = 0

        for n in range(6):
            numerador = x ** (2 * n)
            denominador = factorial(2 * n)
            cos += (-1) ** n / denominador * numerador

        return f"{angulo}° em radianos: {x}" \
               f"\nCosseno de {x}: {cos}"

    return "Valor inválido"

if __name__ == '__main__':

    angulo = int(input("Digite o valor do ângulo em graus: "))
    print(f"\n{cosseno(angulo)}")