'''1. Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.'''

matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for l in range(0,4):
    for c in range (0,4):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30) # linha de separação
for l in range(0,4):
    for c in range(0,4):
        print(f'[{matriz[l][c]:^5}]', end ='')
    print()

maiores_que_10 = 0
for l in range(0,4):
    for c in range(0,4):
        if matriz[l][c] > 10:
            maiores_que_10 += 1

print(f'A matriz M possui {maiores_que_10} números maiores que 10.')