'''
17. Faca uma funcao que receba dois numeros inteiros positivos por parametro e retorne a 
soma dos N numeros inteiros existentes entre eles

'''

def soma_num(num1, num2):
    soma = 0
    
    if num1 > num2 :
        for i in range(num2 + 1, num1):
            soma += i    
    else:
        for i in range(num1 + 1, num2):
            soma += i 
    return soma
print("Informe um numero positivo: ", end=" ")
n1 = int(input())
print("Informe outro numero positivo: ", end=" ")
n2 = int(input())
print(f"Soma: {soma_num(n1,n2)}")