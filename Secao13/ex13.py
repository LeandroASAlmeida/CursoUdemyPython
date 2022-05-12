"""13. Faça um programa que permita que o usuário entre com diversos nomes e telefone para
cadastro, e crie um arquivo com essas informações, uma por linha. O usuário finaliza a
entrada com '0' para o telefone."""

try: #criando arquivo caso não exista
    lista_fone13 = str(input('Nome do arquivo a ser editado, coloque o diretorio onde vai ser criado caso não exista:')) #arquivos\lista-fone13.txt
    arquivo = open(lista_fone13, 'r+')#ler
except FileNotFoundError:
    arquivo = open(lista_fone13, 'w+')#escrever
    arquivo.writelines(u'Arquivo criado pois nao existia\n')

while True:
    nome = (input("Digite um nome : ")).strip().title()
    if len(nome) > 0:
        telefone =(input("Digite um número de telefone ou informe 0 para sair: ")).strip()
        print()

        if len(telefone):
            with open("arquivos/lista-fone13.txt", "a", encoding="utf-8") as arquivo:
                if telefone != '0':
                    informacoes = nome + ";" + telefone
                    arquivo.write(informacoes+"\n")

                else:
                    break

        else:
            print("Telefone inválido!\n")

    else:
        print("\nNome inválido!\n")

print("Informações inseridas no arquivo com sucesso!")








