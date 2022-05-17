"""
Teste de Memória com Generators


# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...

# Teste 1 Lista
for n in fib_lista(100000):
    print(n)

"""

# Função usando listas 449MB

'''
def fib_lista(max): # max =tamamhho da lista 
    nums = []
    a, b = 0, 1 #variaveis
    while len(nums) < max:
        nums.append(b) # adicionando 1 na lista .. pois a sequencia sempre inicia em 1
        a, b = b, a + b
    return nums

print(fib_lista(10)) # imprimi dentro da lista os 10 primeiros numeros dentro da sequencia de fibonati

for n in fib_lista(10): # laço para imprimir a sequencia solta um numero abaixo do outro
    print(n)'''

#Função usando geradores

def fib_gen(max):
    a, b, contador = 0, 1, 0 # variaveis
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 2 Geradores 3MB
for n in fib_gen(100000):
    print(n)'''
