'''21. Faca um programa que leia duas matrizes 2 x 2 com valores reais. Ofereca ao usuario 
um menu de opcoes:
(a) somar as duas matrizes
(b) subtrair a primeira matriz da segunda
(c) adicionar uma constante as duas matrizes `
(d) imprimir as matrizes
Nas duas primeiras opcoes uma terceira matriz 3 x 3 deve ser criada. Na terceira opcao
o valor da constante deve ser lido e o resultado da adicao da constante deve ser arma- 
zenado na propria matriz.'''

matriz_1 = [[0,0],[0,0]]
matriz_2 = [[0,0],[0,0]]
matriz_soma = [[0,0],[0,0]]
matriz_sub = [[0,0],[0,0]]
constante = 0


for l in range(0,2):
    for c in range (0,2):
        matriz_1[l][c] = int(input(f'Digite um valor para [{l},{c}] para a primeira matriz: '))
        matriz_2[l][c] = int(input(f'Digite um valor para [{l},{c}] para a segunda matriz: '))
print('-=' * 30) # linha de separação
print('Selecione uma das opções abaixo: ')
print('-=' * 30) # linha de separação

menu = input('[a]Somar as duas matrizes\n[b]Subtrair a primeira matriz da segunda\n'
             '[c]Adicionar uma constante as duas matrizes\n[d]Imprimir as matrizes\n'
             'opção: ')
while menu != 0:
    if menu == 'a':
        print('Somar as duas matrizes selecionado. ')
        print('MATRIZ SOMA')
        for l in range(0,2):
            for c in range(0,2):
                matriz_soma[l][c] = matriz_1[l][c] + matriz_2[l][c]
                print(f'[{matriz_soma[l][c]:^4}]', end='')
            print()
        print('-=' * 30) # linha de separação
        print('Selecione uma das opções abaixo: ')
        print('-=' * 30) # linha de separação 
        menu = input('[a]Somar as duas matrizes\n[b]Subtrair a primeira matriz da segunda\n'
             '[c]Adicionar uma constante as duas matrizes\n[d]Imprimir as matrizes\n'
             'opção: ')

    elif menu == 'b':
        print('Subtrair as duas matrizes selecionado. ')
        print('MATRIZ SUBTRAÇÃO')
        for l in range(0,2):
            for c in range(0,2):
                matriz_sub[l][c] = matriz_1[l][c] - matriz_2[l][c]
                print(f'[{matriz_sub[l][c]:^4}]', end='')
            print()
        print('-=' * 30) # linha de separação
        print('Selecione uma das opções abaixo: ')
        print('-=' * 30) # linha de separação 
        menu = input('[a]Somar as duas matrizes\n[b]Subtrair a primeira matriz da segunda\n'
             '[c]Adicionar uma constante as duas matrizes\n[d]Imprimir as matrizes\n'
             'opção: ')

    elif menu == 'c':
        constante = int(input("Digite uma constante a ser incluida: "))
        for l in range(0,2):
            for c in range(0,2):
                matriz_1[l][c] += constante
                matriz_2[l][c] += constante
                print(f'[{matriz_1[l][c]:^4}]', end='')
                print(f'[{matriz_2[l][c]:^4}]', end='')
            print()

    elif menu == 'd':
        print('MATRIZ 1')
        for l in range(0,2):
            for c in range(0,2):
                print(f'[{matriz_1[l][c]:^4}]', end='')
            print()
        print('MATRIZ 2')
        for l in range(0,2):
            for c in range(0,2):
                print(f'[{matriz_2[l][c]:^4}]', end='')
            print()
        print('-=' * 30) # linha de separação
        print('Selecione uma das opções abaixo: ')
        print('-=' * 30) # linha de separação 
        menu = input('[a]Somar as duas matrizes\n[b]Subtrair a primeira matriz da segunda\n'
             '[c]Adicionar uma constante as duas matrizes\n[d]Imprimir as matrizes\n'
             'opção: ')
    if menu == '0':
        break