'''
19. Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i+5 * i)%(i+1),
sendo i a posição do elemento no vetor. Em seguida imprima o vetor no ecrã.

'''
valores=[]

for i in range(0,50):
    valores.append((i + 5 * i) % (i + 1))
print(valores)

