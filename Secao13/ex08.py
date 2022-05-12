
"""
8) Faça um programa que leia o conteúdo de um arquivo e crie um arquivo
com o mesmo conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas.
Os nomes dos arquivos serão fornecidos, via teclado, pelo usuário. A função
que converte maiúscula para minúscula é o toupper(). Ela é aplicada em cada caractere da string.
"""



try: #criando arquivo caso não exista
    arquivo_ex08 = str(input('Nome do arquivo a ser editado, coloque o diretorio onde vai ser criado caso não exista:')) #arquivos\arq8.txt
    arquivo = open(arquivo_ex08, 'r+')
except FileNotFoundError:
    arquivo = open(arquivo_ex08, 'w+')
    arquivo.writelines(u'Arquivo criado pois nao existia\n')
    arquivo.writelines(u'Texto Lorem Ipsum pode ser utilizado para voce que esta desenvolvendo seu projeto e precisa de texto aleatorio para preencher os espacos e fazer testes') # escreve diretamente no arquivo criado.


    with open(arquivo_ex08, "r", encoding="utf-8") as arquivo:
        with open("arquivos/arq_novo2.txt", "w", encoding="utf-8") as arquivo_novo:
            arquivo_novo.write(arquivo.read().upper())
    print("\nInformações inseridas no arquivo com sucesso!")


  