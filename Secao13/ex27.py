"""
27. Faça um programa para gerenciar as notas dos alunos de uma turma salva em um arquivo.
O programa deverá ter um menu contendo as seguintes opções:

(a) Definir informações da turma; 
(b) Inserir aluno e notas; 
(c) Exibir alunos e médias; 
(d) Exibir alunos aprovados; 
(e) Exibir alunos reprovados; 
(f) Salvar dados em Disco; 
(g) Sair do programa (fim). 

Faça a rotina que gerencia o menu dentro do main, e para cada uma das opções deste menu, crie uma função específica.

"""
import os
import time
from os import path # caminho local
from os import remove # os.remove()O método em Python é usado para remover ou excluir um caminho de arquivo
   
def verificar_nome(nome):
    caracteres_invalidos = ["-", ":", "?", "/", ">", "<", "}", "{", "[", "]",
                            "+", "*", "@", "!", "%", "¨", ";", "´", "`", "^", "~",
                            "=", "(", ")", "&", "_", "$", "#", ","]

    try:
        for caractere in nome:
            if str(caractere).isnumeric() or str(caractere) in caracteres_invalidos:
                return False

        return True

    except AttributeError:
        return False

    except ValueError:
        return False

    except TypeError:
        return False

def informacoes(arquivo):
  
    try:
        with open(arquivo, "a") as _:
            pass

        with open(arquivo, "r", encoding="utf-8") as leitura:
            print(f"\n\n{'-' * 7}INFORMAÇÕES DA TURMA{'-' * 8}")
            texto = leitura.read().strip().splitlines()

            if len(texto) > 0:
                [print(f"{informacao.replace(';', ' - ')}\n{'-' * 35}") for informacao in texto]

            else:
                print(f"\n{'-' * 35}")

    except ValueError:
        print("-" * 35)

        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 35)

    except FileNotFoundError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 35)

    except OSError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 35)

def inserir_notas(arquivo):

    try:
        with open(arquivo, "a", encoding="utf-8") as insercao:
            print(f"\n\n{'-' * 13}INSERÇÃO{'-' * 14}")

            cod = abs(int(input("Insira o identificador(código) do aluno: ")))

            print("-" * 35)

            codigo_existe = False

            with open(arquivo, "r", encoding="utf-8") as leitura:
                texto = leitura.read().strip().splitlines()

                texto = [informacao.split(";") for informacao in texto]

                for linha in texto:
                    if cod == int(linha[0]):
                        codigo_existe = True

            if not codigo_existe:
                nome = str(input("Insira o nome do aluno: ")).strip().title()
                print("-" * 35)

                if verificar_nome(nome):
                    nota1 = float(input("Insira a primeira nota do aluno: "))
                    print("-" * 35)

                    nota2 = float(input("Insira a segunda nota do aluno: "))
                    print("-" * 35)

                    nota3 = float(input("Insira a terceira nota do aluno: "))
                    print("-" * 35)

                    insercao.write(f"{cod};{nome};{nota1} - {nota2} - {nota3}\n")

                else:
                    print(f"\n\n{'-' * 10}ERRO{'-' * 11}")

                    print("NOME INVÁLIDO!")

                    print("-" * 35)

            else:
                print(f"\n\n{'-' * 10}ERRO{'-' * 11}")

                print("IDENTIFICADOR(CÓDIGO) JÁ EXISTENTE!")

                print("-" * 35)

    except ValueError:
        print("-" * 35)

        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("ERRO AO RECEBER OS DADOS DO USUÁRIO OU AO LER O ARQUIVO!")
        print("-" * 35)

    except FileNotFoundError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 35)

    except OSError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 35)

    except IndexError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 35)

def medias(linha):

    notas = [float(nota) for nota in linha[-1].split(" - ")]

    media = float("{:.1f}".format(float(sum(notas) / len(notas))))

    return media

def alunos_medias(arquivo):
 
    try:
        with open(arquivo, "a", encoding="utf-8") as _:
            pass

        with open(arquivo, "r", encoding="utf-8") as leitura:
            texto = leitura.read().strip().splitlines()

            texto = [informacoes.split(";") for informacoes in texto]

            print(f"\n\n{'-' * 10}ALUNOS E MÉDIAS{'-' * 10}")

            [print(f"{linha[1]} - {medias(linha)}\n{'-' * 35}") for linha in texto]

    except ValueError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 35)

    except FileNotFoundError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 35)

    except OSError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 35)

    except IndexError:
        print(f"\n{'-' * 35}")

        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 35)

def aprovados(arquivo):
 
    try:
        with open(arquivo, "a", encoding="utf-8") as _:
            pass

        with open(arquivo, "r", encoding="utf-8") as leitura:
            texto = leitura.read().strip().splitlines()

            texto = [informacoes.split(";") for informacoes in texto]

            print(f"\n\n{'-' * 12}APROVADOS{'-' * 13}")

            [print(f"{linha[1]}\n{'-' * 35}") for linha in texto if medias(linha) >= 6.0]

    except ValueError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 35)

    except FileNotFoundError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 35)

    except OSError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 35)

    except IndexError:
        print(f"\n{'-' * 35}")

        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 35)

def reprovados(arquivo):

    try:
        with open(arquivo, "a", encoding="utf-8") as _:
            pass

        with open(arquivo, "r", encoding="utf-8") as leitura:
            texto = leitura.read().strip().splitlines()

            texto = [informacoes.split(";") for informacoes in texto]

            print(f"\n\n{'-' * 12}REPROVADOS{'-' * 13}")

            [print(f"{linha[1]}\n{'-' * 35}") for linha in texto if medias(linha) < 6.0]

    except ValueError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 35)

    except FileNotFoundError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 35)

    except OSError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 35)

    except IndexError:
        print(f"\n{'-' * 35}")

        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 35)


if __name__ == "__main__":

    op = 0
    nome_arquivo = "arquivos/turma.txt"

    try:
        while (op != 6 ):
            time.sleep(3)
            os.system('cls')
            print(f"\n\n{'*' *15}MENU{'*' *16}\n")
            print("1 - Definir informações da turma")

            print(f"{'-' * 35}")
            print("2 - Inserir aluno e notas")

            print(f"{'-' * 35}")
            print("3 - Exibir alunos e médias")

            print(f"{'-' * 35}")
            print("4 - Exibir alunos aprovados")

            print(f"{'-' * 35}")
            print("5 - Exibir alunos reprovados")

            print(f"{'-' * 35}")
            print("6 - Sair do programa (fim)")

            print(f"{'-' * 35}")
            opcao = abs(int(input("\nInsira o número da opção que você deseja: ")))

            print(f"{'-' * 35}")

            if opcao == 1:
                informacoes(nome_arquivo)

            elif opcao == 2:
                inserir_notas(nome_arquivo)

            elif opcao == 3:
                medias(nome_arquivo)

            elif opcao == 4:
                aprovados(nome_arquivo)

            elif opcao == 5:
                reprovados(nome_arquivo)

            elif opcao == 6:
                print(f"\n\n{'-' * 10}FIM DO PROGRAMA{'-' * 10}")
                break

            else:
                print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
                print("OPÇÃO INVÁLIDA!")
                print("-" * 35)

    except ValueError:
        print("-" * 35)

        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("OPÇÃO DEVE SER UM NÚMERO INTEIRO!")
        print("-" * 35)
