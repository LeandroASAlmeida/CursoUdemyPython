'''14. Faca um programa para gerar automaticamente numeros entre 0 e 99 de uma cartela de
bingo. Sabendo que cada cartela devera conter 5 linhas de 5 numeros, gere estes dados
de modo a nao ter numeros repetidos dentro das cartelas. O programa deve exibir na 
tela a cartela gerada'''


bingo=0
import numpy as np

for l in range(0,5):
    for c in range (0,5):
        bingo = np.random.randint(1,99)
        print(f"[{bingo:^5}]", end=' ')
    print()
       




