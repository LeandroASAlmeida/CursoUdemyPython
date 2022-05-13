"""
10) Faça um programa que receba o nome de um arquivo de entrada e outro de saída.
O arquivo de entrada contém em cada linha o nome de uma cidade (ocupando 40
caracteres) e o seu número de habitantes. O programa deverá ler o arquivo de
entrada e gerar um arquivo de saída onde aparece o nome da cidade mais populosa
seguida pelo seu número de habitantes.
"""


arquivo_entrada = str(input("Digite o caminho do arquivo de entrada ou o seu nome "
                            "(caso o arquivo esteja no mesmo local do programa): "))#arquivos\listacidade.txt

arquivo_entrada = arquivo_entrada if ".txt" in arquivo_entrada else arquivo_entrada + ".txt"

with open(arquivo_entrada, "r", encoding="utf-8") as arquivo1:
    with open("arquivos/cidade_populosa.txt", "w", encoding="utf-8") as arquivo2:
        linhas = arquivo1.read().strip().splitlines()
        populosa = max(linhas, key=lambda habitantes: int(habitantes[:40:]))
        arquivo2.write(populosa)

    print("\nInformações inseridas no arquivo com sucesso!")



