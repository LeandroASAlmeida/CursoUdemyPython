'''14. Faca um programa para gerar automaticamente numeros entre 0 e 99 de uma cartela de
bingo. Sabendo que cada cartela devera conter 5 linhas de 5 numeros, gere estes dados
de modo a nao ter numeros repetidos dentro das cartelas. O programa deve exibir na 
tela a cartela gerada'''

from random import randint
bingo = [[],[],[],[],[]]
num=int(0)

for l in range(0,5):
    for c in range (0,5):
       while True:
           num = randint(0, 99)
           if num not in bingo:
               bingo[l].append(num)
               break
       print(f"[{bingo[l][c]:^5}]", end=' ')
    print( )
       


