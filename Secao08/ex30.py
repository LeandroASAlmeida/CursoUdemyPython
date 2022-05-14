'''
30. Faca uma func¸ao que receba como parametro o valor de um angulo em graus e calcule 
o valor do cosseno hiperbolico desse  angulo usando sua respectiva serie de Taylor: 
cosh x =
P∞
n=0
x
2n
(2n)! = 1 + x
2
2! +
x
4
4! + . . . para todo x
onde x e o valor do angulo em radianos. Considerar  π = 3.141593 e n variando de 0
ate 5. 

'''


from math import factorial

def cosseno_hiperbolico(angulo):
 
    if angulo > 0:
        pi = 3.141593
        x = angulo * pi / 180
        cosh = 0

        for n in range(6):
            numerador = x ** (2 * n)
            denominador = factorial(2 * n)
            cosh += numerador / denominador

        return f"{angulo}° em radianos: {x}" \
               f"\nCosseno hiperbólico de {x}: {cosh}"

    return "Valor inválido"

if __name__ == '__main__':

    angulo = int(input("Digite o valor do ângulo em graus: "))
    print(f"\n{cosseno_hiperbolico(angulo)}")