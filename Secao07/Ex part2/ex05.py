'''5. Leia uma matriz 5 x 5. Leia tambem um valor X. O programa devera fazer uma busca 
desse valor na matriz e, ao final, escrever a localizacao (linha e coluna) ou uma mensa- 
gem de “nao encontrado'''

matriz=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
linha_x = 0
coluna_x= 0
vlr_x=0
cont=0

for l in range(0,5):
    for c in range (0,5):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30) # linha de separação
for l in range(0,5):
    for c in range(0,5):
        print(f'[{matriz[l][c]:^5}]', end ='')
    print()

vlr_x = int(input("Digite um valor para ser procurado na matriz: "))
for l in range(0,5):
    for c in range(0,5):
        if matriz[l][c] == vlr_x:
            print(f"O valor {vlr_x} se encontra na posição [{l}][{c}] na matriz.")
        elif matriz[l][c] != vlr_x:
            cont += 1
if cont == 25:
    print("Não encontrado.")