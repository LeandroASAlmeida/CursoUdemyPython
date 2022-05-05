'''
Faça uma função 'Troque', que recebe duas variaveis reais A e B e troca o valor delas (i.e. ,A recebe o valor de B e B recebe o valor de A)

'''

def troque(num_a, num_b):
    a = num_a
    b = num_b
    
print("Informe o valor de A : ", end=" ")
a = float(input())
print("Informe o valor de B : ", end=" ")
b = float(input())
print("\nOriginais: A -> ", a," / B -> ", b)
troque(a, b)
print("\nInversos: A -> ", b," / B -> ", a)
