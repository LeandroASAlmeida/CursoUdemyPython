'''4. Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois
valores X e Y quaisquer correspondentes a duas posições no vetor. No final o seu
programa deverá escrever a soma dos valores encontrados nas respetivas posições X e
Y .'''

valores=[]

for n in range(0,8):
    num =int(input('Informe 6 valores inteiros: '))
    valores.append(num)

x = int(input(f"Escolha uma das posições do vetor para a soma (de 0 à 7):\n{valores}"))
y = int(input(f"Escolha uma outra posição do vetor para a soma (de 0 à 7):\n{valores}"))

if 0 < x < 8 and 0 < y < 8:
    soma = valores[x] + valores[y]
    print(f"A soma entre o valor {valores[x]} (indice {x}) e {valores[y]} (indice {y}) é de {soma}.")
else:
    x = int(input("Escolha uma das posições do vetor para a soma (de 0 à 7): "))
    y = int(input("Escolha uma outra posição do vetor para a soma (de 0 à 7) "))


