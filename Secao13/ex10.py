"""
10) Faça um programa que receba o nome de um arquivo de entrada e outro de saída.
O arquivo de entrada contém em cada linha o nome de uma cidade (ocupando 40
caracteres) e o seu número de habitantes. O programa deverá ler o arquivo de
entrada e gerar um arquivo de saída onde aparece o nome da cidade mais populosa
seguida pelo seu número de habitantes.
"""


arquivo_entrada = str(input("Digite o caminho do arquivo de entrada ou o seu nome: "))#arquivos\cidades.txt

arquivo_entrada = arquivo_entrada if ".txt" in arquivo_entrada else arquivo_entrada + ".txt"

try:
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

        hab = [[int(caracter) for caracter in linha.split() if caracter.isdigit()] for linha in linhas]
        cidade = [linha[:linha.index('  ')] for linha in linhas]

        dict_cidades = {cidade[i]: hab[i][0] for i in range(len(linhas))}

        mais_populosa = (max(dict_cidades, key=lambda habitantes: dict_cidades[habitantes]))

    with open('cidade_populosa.txt', 'w', encoding='utf-8') as arquivo2:
        arquivo2.write(mais_populosa + ' ')
        arquivo2.write(str(dict_cidades[mais_populosa]))
        print('\nArquivo "cidade_mais_populosa.txt" criado com sucesso')

except FileNotFoundError:
    print(f'Arquivo "{arquivo_entrada}" não encontrado ')