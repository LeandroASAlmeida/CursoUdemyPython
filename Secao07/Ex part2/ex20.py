'''20. Faca programa que leia uma matriz 3 x 6 com valores reais.
(a) Imprima a soma de todos os elementos das colunas ımpares.
(b) Imprima a media aritmetica dos elementos da segunda e quarta colunas.
(c) Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.
(d) Imprima a matriz modificada.'''



matriz = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
somaimpar =float()
soma = float()
divisor = float()

for l in range(0,3):
    for c in range(0,6):
        matriz[l][c] = float(input(f"Defina um valor para a posição [{l}][{c}]: "))

print('-=' * 30) # linha de separação
for l in range(0,3):
    for c in range(0,6):
        print(f"[{matriz[l][c]:^10}]", end='')
    print( )

for l in range(0,3):
    for c in range(0,6):
        if c % 2 == 0:
            somaimpar += matriz[l][c]
        if l == 1 or c == 3:
            soma += matriz[l][c]
            divisor += 1
        if c == 5:
            matriz[l][c] = matriz[l][0] + matriz[l][1]

media_aritmetica = soma / divisor

print(f"Soma das colunas impares: {somaimpar}\nMédia aritmética da segunda e"
      f" quarta coluna: {media_aritmetica}\nMatriz modificada: ")

print('-=' * 30) # linha de separação
for l in range(3):
    for c in range(6):
        print(f"[{matriz[l][c]:^10}]", end='')
    print( )


