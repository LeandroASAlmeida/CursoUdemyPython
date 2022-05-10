'''
70) Um racional é qualquer número da forma p/q, sendo p inteiro e q inteiro
não nulo. é conveniente representar um racional por registro:
    struct racional{
        int p, q;
    };
Vamos convecionar que o campo q de todo racional é estritamente positivo e que
o máximo divisor comum dos campos p e q é 1. Escreva
(a) uma função reduz que receba inteiros a e b e devolva o racional que representa a/b;
(b) uma função neg que receba um racional x e devolva o racional -x;
(c) uma função soma que receba racionais x e y e devolva o racional que representa a
soma de x e y;
(d) uma função mult que receba racionais x e y e devolva o racional que representa o
produto de x por y;
(e) uma função div que receba racionais x e y e devolva o racional que representa o quociente
de x por y;
'''

def reduz(a, b):

    if type(a) == int and type(b) == int:
        if a > 0 and b > 0:
            return a / b


def neg(x):


    if type(x) == int or type(x) == float:
        if x > 0:
            return x * (-1)


def soma(x, y):
  

    if type(x) == int or type(x) == float:
        if type(y) == int or type(y) == float:
            if x > 0 and y > 0:
                return x + y


def mult(x, y):

    if type(x) == int or type(x) == float:
        if type(y) == int or type(y) == float:
            if x > 0 and y > 0:
                return x * y


def div(x, y):


    if type(x) == int or type(x) == float:
        if type(y) == int or type(y) == float:
            if x > 0 and y > 0:
                return x / y


if __name__ == '__main__':

    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um número: "))

    print(f"\nRacional de {num1} / {num2}: {reduz(num1, num2)}")
    print(f"Número {num1} negativo: {neg(num1)}")
    print(f"Número {num2} negativo: {neg(num2)}")
    print(f"Soma de {num1} por {num2}: {soma(num1, num2)}")
    print(f"Produto de {num1} por {num2}: {mult(num1, num2)}")
    print(f"Quociente de {num1} por {num2}: {div(num1, num2)}")