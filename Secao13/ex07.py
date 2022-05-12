
"""
7) Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo
texto contendo o texto do arquivo de entrada, mas com as vogais substituídas por '*'
"""


def substitui_vogais(txt):

        vogais = ['a', 'e', 'i', 'o', 'u']

        for vogal in vogais:
            txt = txt.replace(vogal.lower(), "*")#O replace()método substitui uma entrada especificada por outra entrada especificada.
            txt = txt.replace(vogal.upper(), "*")#O replace()método substitui uma entrada especificada por outra entrada especificada.

        return txt

if __name__ == "__main__":

    try: #criando arquivo caso não exista
        arquivo_ex07 = str(input('Nome do arquivo a ser editado, coloque o diretorio onde vai ser criado caso não exista:')) #arquivos\arq7.txt
        arquivo = open(arquivo_ex07, 'r+')
    except FileNotFoundError:
        arquivo = open(arquivo_ex07, 'w+')
        arquivo.writelines(u'Arquivo criado pois nao existia\n')
        arquivo.writelines(u'Texto Lorem Ipsum pode ser utilizado para voce que esta desenvolvendo seu projeto e precisa de texto aleatorio para preencher os espacos e fazer testes') # escreve diretamente no arquivo criado.

    arquivo.close()

    with open(arquivo_ex07, "r", encoding="utf-8") as arquivo:
        with open("arquivos/arq_novo.txt", "w", encoding="utf-8") as arquivo_novo:
            arquivo_novo.write(substitui_vogais(arquivo.read()))
        print("\nTexto inserido no novo arquivo com sucesso!")

