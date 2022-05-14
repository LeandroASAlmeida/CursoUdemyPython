'''25. Faca um programa para determinar a proxima jogada em um Jogo da Velha. Assumir que 
o tabuleiro e representado por uma matriz de 3 x 3, onde cada posic ao representa uma 
das casas do tabuleiro. A matriz pode conter os seguintes valores -1, 0, 1 representando
respectivamente uma casa contendo uma peca minha (-1), uma casa vazia do tabuleiro
(0), e uma casa contendo uma peca do meu oponente (1).
Exemplo:
-1 1 1
-1 -1 0
 0 1 0'''

jogo = []

for i in range(3):
    velha = []
    for j in range(3):
        velha.append(0)
    jogo.append(velha)

cont = 1
continua = True 
vezes = 0

print(f"\n\n{'*' *15}JOGO DA VELHA{'*' *16}\n")

while continua:
    for i in range(3):
        for j in range(3):
            print(jogo[i][j], end='  ')
        print()

    if cont % 2 == 0:
        print("\nJOGADOR 2 = '-1'")

    elif cont % 2 == 1:
        print("\nJOGADOR 1 = '1'")

    linha = int(input("Qual a linha da sua jogada?(1 a 3): "))
    if (linha >= 1) and (linha <= 3):
        coluna = int(input("Qual a coluna da sua jogada? (1 a 3): "))

        if (coluna >= 1) and (coluna <= 3):
            if cont % 2 == 0:
                if jogo[linha-1][coluna-1] == 0:
                    jogo[linha-1][coluna-1] = -1

                    vezes += 1

                else:
                    print("Jogada invalida\n")

            elif cont % 2 == 1:
                if jogo[linha-1][coluna-1] == 0:
                    jogo[linha-1][coluna-1] = 1
                    vezes += 1

                else:
                    print("Jogada invalida\n")

        else:
            print("Coluna Invalida\n")
            cont += 1
            continue

    else:
        print("Linha Invalida\n")
        cont += 1
        continue

    for i in range(-1, 2, 1):
        if (i == -1) or (i == 1):
            for j in range(3):
                # velha na horizontal
                if jogo[j][0] == i and jogo[j][1] == i and jogo[j][2] == i:
                    print(f"\nJOGADOR '{i}' GANHOU!!")
                    continua = False
                    break

                # velha na vertical
                elif jogo[0][j] == i and jogo[1][j] == i and jogo[2][j] == i:
                    print(f"\nJOGADOR '{i}' GANHOU!!")
                    continua = False
                    break

                # velha na diagonal principal
                elif jogo[0][0] == i and jogo[1][1] == i and jogo[2][2] == i:
                    print(f"\nJOGADOR '{i}' GANHOU!!")
                    continua = False
                    break

                # velha na diagonal inversa
                elif jogo[0][2] == i and jogo[1][1] == i and jogo[2][0] == i:
                    print(f"\nJOGADOR '{i}' GANHOU!!")
                    continua = False
                    break

    # empate 
    if continua and vezes >= 9:
        print("\nEMPATE")
        continua = False

    # Imprimir o jogo
    if not continua:
        print()
        for i in range(3):

            for j in range(3):
                print(jogo[i][j], end='  ')

            print()

    cont += 1

