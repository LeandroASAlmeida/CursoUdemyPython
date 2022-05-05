'''
31. Faca uma funcao para calcular o 'numero neperiano' usando uma serie. A funcao deve 
ter como parametro o numero de termos que serao somados (note que, quanto maior o 
numero, mais proxima a resposta estara do valor e).
` =
P∞
n=0
1
n! =
1
0! +
1
1! +
1
2! +
1
3! +
1
4! + . . 

'''

from math import factorial


def numero_neperiano(numero):
 
    if (numero >= 0) and (numero // 1 == numero):
        calculo = 0
        numerador = 1

        for i in range(numero):
            denominador = factorial(i)
            calculo += numerador / denominador
        return calculo


num = int(input("Informe quantos termos a serem calculados: "))
print(f"\nNúmero neperiano: {numero_neperiano(num)}")




