'''
13. Faca uma funcao que receba dois valores numericos e um sımbolo. Este sımbolo representara a operacao que se deseja efetuar com os numeros. Se o sımbolo for + devera
ser realizada uma adicao, se for  uma subtracao, se for  / uma divisao e se for sera
efetuada uma multiplicacao.

'''

def operacao(num1, num2, op):
    if op == "+":
        return f"Soma: {num1+num2}"
    elif op == "-":
        return f"Subtração: {num1-num2}"
    elif op == "*":
        return f"Multiplicação: {num1*num2}"
    elif op == "/":
        return f"Divisão: {num1/num2}"
    else:
        return "Operador Invalido"
    
print("Informe o 1° numero: ", end=" ")
n1 = float(input())
print("Informe o 2° numero: ", end=" ")
n2 = float(input())
print("""\n
 Informe a operação:
 + -> Soma
 - -> Subtração
 * -> Multiplicação
 / -> Divisão
 Operação: """, end=" ")
op = input()
print("\n", operacao(n1, n2, op))