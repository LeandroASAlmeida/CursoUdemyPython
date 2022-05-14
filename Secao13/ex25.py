"""
25. Faça um programa gerenciar uma agenda de contatos. Para cada contato armazene o
nome, o telefone e o aniversário (dia e mês). O programa deve permitir
(a) inserir contato
(b) remover contato 
(c)pesquisar um contato pelo nome 
(d) listar todos os contatos 
(e) listar os contatos cujo nome inicia com uma dada letra 
(f) imprimir os aniversariantes do mês.
Sempre que o programa for encerrado, os contatos devem ser armazenados em um arquivo binário. 
Quando o programa iniciar, os contatos devem ser inicializados com os dados contidos neste arquivo binário.

"""

import os
import time
from datetime import date

   
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

def verificar_telefone(telefone):



    caracteres_validos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ",
                          "+", "(", ")", "-"]

    try:
        valido = False
        for caractere in str(telefone):
            if str(caractere) in caracteres_validos:
                valido = True

            else:
                valido = False
                break

        return valido

    except AttributeError:
        return False

    except ValueError:
        return False

def inserir(arquivo):

    try:
        with open(arquivo, "ab") as insercao:
            print(f"\n\n{'-' * 11}INSERÇÃO{'-' * 13}")

            cod = abs(int(input("Digite o identificador(código) do contato: ")))

            print("-" * 30)

            codigo_existe = False

            with open(arquivo, "rb") as leitura:
                informacoes = leitura.read().decode("utf8").strip().splitlines()
                informacoes = [infor.split(";") for infor in informacoes]

                for linha in informacoes:
                    if int(linha[0]) == cod:
                        codigo_existe = True

            if codigo_existe:
                print(f"\n\n{'-' * 13}ERRO{'-' * 14}")

                print("O IDENTIFICADOR(CÓDIGO) JÁ EXISTE!")

                print("-" * 30)

            else:
                nome = str(input("Digite o nome do contato: ")).strip().title()
                print("-" * 30)

                if verificar_nome(nome):
                    telefone = str(input(f"Informe o número do telefone de {nome}: "))
                    print("-" * 30)

                    if verificar_telefone(telefone):
                        mm = abs(int(input(f"Informe o mês do aniversário de {nome}: ")))
                        print("-" * 30)

                        dd = abs(int(input(f"Informe o dia do aniversário de {nome}: ")))
                        print("-" * 30)

                        if ((mm > 0) and (mm < 13)) and ((dd > 0) and (dd < 32)):
                            mes = str(mm)
                            dia = str(dd)

                            if len(mes) == 1:
                                mes = "0"+mes

                            if len(dia) == 1:
                                dia = "0"+dia

                            insercao.write(f"{cod};{nome};{telefone};{dia}/{mes}\n".encode("utf8"))

                            print(f"\n\n{'-' * 11}INFORMAÇÃO{'-' * 11}")

                            print("CONTATO INSERIDO COM SUCESSO!")

                            print("-" * 30)

                        else:
                            print(f"\n\n{'-' * 13}ERRO{'-' * 14}")

                            print("DATA INVÁLIDA(VALORES FORA DO INTERVALO PERMITIDO)!")

                            print("-" * 30)

                    else:
                        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")

                        print("TELEFONE INVÁLIDO!")

                        print("-" * 30)

                else:
                    print(f"\n\n{'-' * 13}ERRO{'-' * 14}")

                    print("NOME INVÁLIDO!")

                    print("-" * 30)

    except ValueError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("ERRO AO RECEBER OS DADOS DO USUÁRIO OU AO LER O ARQUIVO!")
        print("-" * 30)

    except FileNotFoundError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 30)

    except OSError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 30)

    except IndexError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)

def deletar(arquivo):
  
    try:
        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as conteudo:
            informacoes = conteudo.read().decode("utf8").strip().splitlines()

            if len(informacoes) > 0:
                informacoes = [infor.split(";") for infor in informacoes]

                print(f"\n\n{'-' * 13}DELEÇÃ0{'-' * 13}")

                cod = abs(int(input(" Qual o codigo do contato que você deseja deletar: ")))

                print("-" * 30)

                with open(arquivo, "wb") as delecao:
                    codigo_existe = False

                    for linha in informacoes:
                        if int(linha[0]) == cod:
                            informacoes.remove(linha)
                            codigo_existe = True

                    for linha in informacoes:
                        delecao.write(f"{linha[0]};{linha[1]};{linha[2]};{linha[3]}\n".encode("utf8"))

                    if codigo_existe:
                        print(f"\n\n{'-' * 11}INFORMAÇÃO{'-' * 11}")

                        print("CONTATO DELETADO COM SUCESSO!")

                        print("-" * 30)

                    else:
                        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")

                        print("IDENTIFICADOR(CÓDIGO) NÃO EXISTENTE!")

                        print("-" * 30)

            else:
                print(f"\n\n{'-' * 13}ERRO{'-' * 14}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 30)

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("ERRO AO RECEBER OS DADOS DO USUÁRIO OU AO LER O ARQUIVO!")
        print("-" * 30)

    except FileNotFoundError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 30)

    except OSError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 30)

    except IndexError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)

def pesquisar_por_nome(arquivo):

    try:
        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as leitura:
            texto = leitura.read().decode("utf8").strip().splitlines()

            if len(texto) > 0:
                texto = [informacoes.split(";") for informacoes in texto]

                print(f"\n\n{'-' * 11}PESQUISAR POR NOME{'-' * 13}")
                nome = str(input("Digite o nome do contato: ")).strip().title()
                print("-" * 30)

                if verificar_nome(nome):
                    existe = False

                    print(f"\n\n{'-' * 11}CONTATOS{'-' * 13}")

                    for informacoes in texto:
                        if informacoes[1].strip().title() == nome:
                            print(f"{informacoes[0]} - {informacoes[1]} - {informacoes[2]} - {informacoes[3]}"
                                  f"\n{'-' * 30}")

                            existe = True

                    if not existe:
                        print(f"\n{'-' * 30}")

                else:
                    print(f"\n\n{'-' * 13}ERRO{'-' * 14}")

                    print("OS NOMES DOS CONTATOS NÃO CONTÉM CARACTERES ESPECIAIS OU NÚMEROS!")

                    print("-" * 30)

            else:
                print(f"\n\n{'-' * 13}ERRO{'-' * 14}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 30)

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 30)

    except FileNotFoundError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 30)

    except OSError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 30)

    except IndexError:
        print(f"\n{'-' * 30}")

        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)

def listar_contatos(arquivo):


    try:
        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as leitura:
            print(f"\n\n{'-' * 6}LISTA DE CONTATOS{'-' * 6}")
            texto = leitura.read().decode("utf8").strip().splitlines()

            if len(texto) > 0:
                [print(f"{informacao.replace(';', ' - ')}\n{'-' * 30}") for informacao in texto]

            else:
                print(f"\n{'-' * 30}")

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 30)

    except FileNotFoundError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 30)

    except OSError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 30)

def pesquisar_por_letra(arquivo):

    try:
        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as leitura:
            texto = leitura.read().decode("utf8").strip().splitlines()

            if len(texto) > 0:
                texto = [informacoes.split(";") for informacoes in texto]

                print(f"\n\n{'-' * 11}PESQUISAR POR LETRA{'-' * 11}")

                letra = str(input("Digite uma letra: ")).strip().title()[0]

                print("-" * 30)

                print(f"\n\n{'-' * 11}CONTATOS{'-' * 13}")

                existe = False

                for informacoes in texto:
                    if informacoes[1].strip().title()[0] == letra:
                        print(f"{informacoes[0]} - {informacoes[1]} - {informacoes[2]} - {informacoes[3]}"
                              f"\n{'-' * 30}")

                        existe = True

                if not existe:
                    print(f"\n{'-' * 30}")

            else:
                print(f"\n\n{'-' * 13}ERRO{'-' * 14}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 30)

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 30)

    except FileNotFoundError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 30)

    except OSError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 30)

    except IndexError:
        print(f"\n{'-' * 30}")

        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)

def aniversariante_do_mes(arquivo):


    mes_atual = date.today().month

    try:
        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as leitura:
            texto = leitura.read().decode("utf8").strip().splitlines()

            if len(texto) > 0:
                texto = [informacoes.split(";") for informacoes in texto]

                print(f"\n\n{'-' *3}ANIVERSARIANTES DO MÊS{'-' * 3}")

                existe = False

                for informacoes in texto:
                    if int(informacoes[-1].strip()[-2::]) == int(mes_atual):
                        print(f"{informacoes[1]}\n{'-' * 30}")

                        existe = True

                if not existe:
                    print(f"\n{'-' * 30}")

            else:
                print(f"\n\n{'-' * 13}ERRO{'-' * 14}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 30)

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 30)

    except FileNotFoundError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 30)

    except OSError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 30)

    except IndexError:
        print(f"\n{'-' * 30}")

        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)


if __name__ == "__main__":

    opcao = 0
    nome_arquivo = "arquivos/contatos.bin"

    try:
        while (opcao != 7 ):
            time.sleep(3)
            os.system('cls')

            print(f"\n\n{'+' * 11} AGENDA {'+' * 11}")
            print("1 - Inserir um contato")

            print(f"{'-' * 30}")
            print("2 - Deletar um contato")

            print(f"{'-' * 30}")
            print("3 - Pesquisar pelo nome")

            print(f"{'-' * 30}")
            print("4 - Listar os contatos")

            print(f"{'-' * 30}")
            print("5 - Listar dada letra")

            print(f"{'-' * 30}")
            print("6 - Aniversariantes do mês")

            print(f"{'-' * 30}")
            print("7 - Fechar agenda")

            print(f"{'-' * 30}")
            opcao = abs(int(input("\nDigite o número da opção que você deseja: ")))

            print(f"{'-' * 30}")

            if opcao == 1:
                inserir(nome_arquivo)

            elif opcao == 2:
                deletar(nome_arquivo)

            elif opcao == 3:
                pesquisar_por_nome(nome_arquivo)

            elif opcao == 4:
                listar_contatos(nome_arquivo)

            elif opcao == 5:
                pesquisar_por_letra(nome_arquivo)

            elif opcao == 6:
                aniversariante_do_mes(nome_arquivo)

            elif opcao == 7:
                print(f"\n\n{'-' * 12}AGENDA FECHADA- OBRIGADO!{'-' * 13}")
                break

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 14}")
        print("OPÇÃO INVÁLIDA!")
        print("-" * 30)
