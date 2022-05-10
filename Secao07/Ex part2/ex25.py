'''25. Faca um programa para determinar a proxima jogada em um Jogo da Velha. Assumir que 
o tabuleiro e representado por uma matriz de 3 x 3, onde cada posic ao representa uma 
das casas do tabuleiro. A matriz pode conter os seguintes valores -1, 0, 1 representando
respectivamente uma casa contendo uma peca minha (-1), uma casa vazia do tabuleiro
(0), e uma casa contendo uma peca do meu oponente (1).
Exemplo:
-1 1 1
-1 -1 0
 0 1 0'''

jogador1=-1
jogador2=1

velha = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('-=' * 30) # linha de separação
for l in range(0,3):
    for c in range(0,3):
        print(f'[{velha[l][c]:^5}]', end ='')
    print()
print('-=' * 30) # linha de separação
