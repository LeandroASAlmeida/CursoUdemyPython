
'''
33. Faca uma funcao que receba um numero N e retorne a soma dos algarismos de N!. Ex: 
se N = 4, N! = 24. Logo, a soma de seus algarismos e 2 + 4 = 6.
'''

def soma_fatorial(n):
    fat =1
    soma=0
    
    for i in range(1, n+1):
        fat *= i
    fat = list(str(fat))
    
    for i in range(len(fat)):
        soma += int(fat[i])
        
    return soma
print("Informe um numero inteiro: ", end=" ")
num = int(input())
print(f"A soma dos Algarismos é : {soma_fatorial(num)}")


