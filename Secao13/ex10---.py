"""
10) Faça um programa que receba o nome de um arquivo de entrada e outro de saída.
O arquivo de entrada contém em cada linha o nome de uma cidade (ocupando 40
caracteres) e o seu número de habitantes. O programa deverá ler o arquivo de
entrada e gerar um arquivo de saída onde aparece o nome da cidade mais populosa
seguida pelo seu número de habitantes.
"""

'''arquivo_ex10 = str(input("Informe o caminho do diretorio onde se encontra o arquivo: ")) #arquivos\arq10.txt

with open(arquivo_ex10, "r", encoding="utf-8") as arquivo1:
    with open("arquivos/cidade_populosa.txt", "w", encoding="utf-8") as arquivo2:
        linhas = arquivo1.read().strip().splitlines()
        populosa = max(linhas, key=lambda habitantes: int(habitantes[40::]))
        arquivo2.write(populosa)

print("\nInformações inseridas no arquivo com sucesso!")
'''

try: #criando arquivo caso não exista
    arquivo_ex10 = str(input('Nome do arquivo a ser editado, coloque o diretorio onde vai ser criado caso não exista:')) #arquivos\arq10.txt
    arquivo = open(arquivo_ex10, 'r+')
except FileNotFoundError:
    arquivo = open(arquivo_ex10, 'w+')
    arquivo.writelines(u'Arquivo criado pois nao existia\n')
    arquivo.writelines(u'Sao Paulo- brasil -  3215422222214111111\n'
                        'Campinas- brasil -  32154222222229999111\n'
                        'Osasco- brasil -  3666666666666666666661\n') # escreve diretamente no arquivo criado.

with open(arquivo_ex10, "r", encoding="utf-8") as arquivo1:
    with open("arquivos/cidade_populosa.txt", "w", encoding="utf-8") as arquivo2:
        linhas = arquivo1.read().strip().splitlines()
    

print("\nInformações inseridas no arquivo com sucesso!")


##nomes = [dado[0:40:1] for dado in informacoes]

