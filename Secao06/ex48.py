'''
Faca um programa que some os termos de valor par da sequencia de Fibonacci, cujos
valores nao ultrapassem quatro milhoes

'''
a = 0 # O termo de Fibonacci sempre começa com 0 e 1 , logo os próximos termos é a soma   do atual mais o práoximo numero.  Onde a varival inicial é ZERO
b = 1 # e a b sempre vai ser a que vai acrescentar a soma
soma = 0

while(b < 4_000_000):
    c = a
    a = b
    b = a + c
    if b %  2 == 0:
        soma += b
print(soma)

