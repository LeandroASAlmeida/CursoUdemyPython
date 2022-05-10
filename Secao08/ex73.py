"""
73) Foi realizada uma pesquisa de algumas características físicas de cinco
habitantes de certa região. De cada habitante foram coletados os seguintes
dados: sexo, cor dos olhos (A - Azuis ou C - Castanhos), cor dos cabelos
(L - Louros, P - Pretos ou C - Castanhos) e idade
    . Faça uma função que leia esses dados em um vetor
    . Faça uma função que determine a média de idade das pessoas
    com olhos castanhos e cabelos pretos
    . Faça uma função que determine e devolva ao programa principal a maior
    idade entre os habitantes
    . Faça uma função que determine e devolva ao programa principal a quantidade
    de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que
    tenham olhos azuis e cabelos louros
"""


def ler_dados():
 
    habitantes = []

    for i in range(0,5):
        informacoes = []

        sexo = ''
        while not(sexo == "M" or sexo == "F"):
            sexo = str(input(f"QUALO SEXO DO HABITENTE {i+1} ?:  (M = masculino / F = feminino): "))
            sexo = sexo.upper()
        informacoes.append(sexo.upper())

        cor_olhos = ''
        while not(cor_olhos == "A" or cor_olhos == "C"):
            cor_olhos = str(input(f"COR DOS OLHOS DO HABITANTE {i+1}?:  (A = azuis / C = castanhos): "))
            cor_olhos = cor_olhos.upper()
        informacoes.append(cor_olhos.upper())

        cor_cabelos = ''
        while not(cor_cabelos == "L" or cor_cabelos == "P" or cor_cabelos == "C"):
            cor_cabelos = str(input(f"COR DO CABELO DO HABITENTE {i+1}?: (L = Louro / P = Preto / C = Castanho): "))
            cor_cabelos = cor_cabelos.upper()
        informacoes.append(cor_cabelos.upper())

        idade = int(input(f"IDADE DO HABITANTE {i+1}: ? "))
        informacoes.append(idade)

        print()
        print('-=' * 30) # linha de separação

        habitantes.append(informacoes)

    return habitantes


def media(args):

    dados1 = True

    if len(args) == 5:
        for i in range(len(args)):
            if len(args[i]) != 4:
                dados1 = False

    else:
        dados1 = False

    if dados1:
        soma_idade = 0
        qtd = 0

        for i in range(5):

            if args[i][1] == 'C':
                if args[i][2] == 'P':
                    soma_idade += args[i][3]
                    qtd += 1

                    print(f"Média de idade das pessoas com olhos castanhos e cabelos pretos: {int(soma_idade / qtd)}")

    else:
        print("Dados inválidos")


def maior_idade(args):

    dados2 = True

    if len(args) == 5:
        for i in range(len(args)):
            if len(args[i]) != 4:
                dados2 = False

    else:
        dados2 = False

    if dados2:
        maior = []

        for i in range(5):
            maior.append(args[i][3])

        return max(maior)


def qtd_individuos(args):

    dados3 = True

    if len(args) == 5:
        for i in range(len(args)):
            if len(args[i]) != 4:
                dados3 = False

    else:
        dados3 = False

    if dados3:
        quantidade = 0

        for i in range(5):
            if args[i][0] == 'F' and args[i][1] == 'A':
                if (args[i][0] == 'F') and (args[i][3] >= 18) and (args[i][3] <= 35):
                    quantidade += 1

        return quantidade

if __name__ == '__main__':

    dados = ler_dados()
    media(dados)
    print(f"A maior idade entre os habitantes: {maior_idade(dados)}")
    print(f"Quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) "
        f"e que tenham olhos azuis e cabelos louros: {qtd_individuos(dados)}")