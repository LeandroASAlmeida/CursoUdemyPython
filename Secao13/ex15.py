"""
15. Faça um programa que receba como entrada o ano corrente e o nome de dois arquivos:
um de entrada e outro de saída. Cada linha do arquivo de entrada contém o nome de uma pessoa (ocupando 40 caracteres) 
e o seu ano de nascimento. O programa deverá ler o arquivo de entrada e 
gerar um arquivo de saída onde aparece o nome da pessoa seguida por uma string que representa a sua idade.

"""
ano_corrente = int(input("Digite o ano corrente: "))

try: #criando arquivo caso não exista
    arquivo_ex15 = str(input('Nome do arquivo a ser editado, coloque o diretorio onde vai ser criado caso não exista:')) #arquivos\arq15.txt
    arquivo = open(arquivo_ex15, 'r+')#ler
except FileNotFoundError:
    arquivo = open(arquivo_ex15, 'w+')#escrever
    arquivo.writelines(u'Arquivo criado pois nao existia\n')
    arquivo.write("Joao -  2005                            \n")
    arquivo.write("Maria -  1988                           \n")
    arquivo.write("Pedro -  1986                           \n")
    arquivo.write("Jose -  1963                           \n")
    arquivo.write("Felipe -  1995                          \n")

with open(arquivo_ex15, "r", encoding="utf-8") as arquivo:
    arquivo15_2 = str(input('Nome do arquivo a ser editado, coloque o diretorio onde vai ser criado caso não exista:'))#arquivos\novo15.txt
    informacoes = arquivo.read().splitlines()

    nomes = [dado[0:40:1] for dado in informacoes]
    ano_nascimento = [dado[41::] for dado in informacoes]

    with open(arquivo15_2 , "w", encoding="utf-8") as novo_arquivo:
        for linha in range(len(nomes)):
            nome = nomes[linha].strip()
            idade = ano_corrente - int(ano_nascimento[linha])

            if idade < 18:
                    novo_arquivo.write(f"{nome}: menor de idade\n")

            elif idade > 18:
                    novo_arquivo.write(f"{nome}: maior de idade\n")

            else:
                novo_arquivo.write(f"{nome}: entrando na maior idade\n")

        print("\nInformações inseridas no arquivo com sucesso!")