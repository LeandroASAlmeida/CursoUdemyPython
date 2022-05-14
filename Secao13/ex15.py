"""
15. Faça um programa que receba como entrada o ano corrente e o nome de dois arquivos:
um de entrada e outro de saída. Cada linha do arquivo de entrada contém o nome de uma pessoa (ocupando 40 caracteres) 
e o seu ano de nascimento. O programa deverá ler o arquivo de entrada e 
gerar um arquivo de saída onde aparece o nome da pessoa seguida por uma string que representa a sua idade.

"""
from datetime import date



def calculo_idade(born):
    hoje = date.hoje()
    try:
        niver = born.replace(year=hoje.year)
    except ValueError:
        niver = born.replace(year=hoje.year,
                                month=born.month + 1, day=1)
    if niver > hoje:
        return hoje.year - born.year - 1
    else:
        return hoje.year - born.year

def string_idade(idade_):
    if idade_ > 18:
        return 'maior de idade'
    elif idade_ == 18:
        return 'entrando na maior idade'
    else:
        return 'menor de idade'



nome_arquivo = str(input("Digite o caminho do arquivo ou o seu nome: "))

nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo + ".txt"

try:
    with open('niver15.txt', 'r', encoding='utf-8') as arquivo_1:
        linhas = arquivo_1.readlines()

        # Cria uma lista separando as informacoes, onde o ultimo elemento da lista é a data de nascimento
        informacao = [linhas[i].strip().split() for i in range(len(linhas))]

        # Criar outra lista retirando a data do final da linha e separando dia,mes e ano
        data_nasc = [informacao[i].pop().split("/") for i in range(len(informacao))]
        data_nasc = [[int(data) for data in pessoa] for pessoa in data_nasc]   # transformar a data em inteiro
        idade = (calculo_idade(date(data_nasc[i][2], data_nasc[i][1], data_nasc[i][0]))  # calcular a idade
                 for i in range(len(informacao)))
        data_nasc = [string_idade(i) for i in idade]

        with open('nomes_string.txt', 'w', encoding='utf-8')as arquivo_2:
            for i in range(len(informacao)):

                arquivo_2.write(f'{" ".join(informacao[i])}  ' f': {data_nasc[i]}\n')

except FileNotFoundError:
    print("O arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")