"""
24. Implemente um controle simples de mercadorias em uma despensa doméstica. Para
cada produto armazene um código numérico, descrição e quantidade atual.
O programa deve ter opções para entrada e retirada de produtos,
bem como um relatório geral e um de produtos não disponíveis. Armazene os dados em arquivo binário.

"""

import os
import time

def inserir(arquivo):

    try:
        with open(arquivo, "ab") as insercao:
            print(f"\n\n{'-' * 13}INSERÇÃO{'-' * 13}")
            cod = abs(int(input("Digite o código numérico do produto: ")))

            print("-" * 30)

            codigo_existe = False

            with open(arquivo, "rb") as leitura:
                informacoes = leitura.read().decode("utf8").strip().splitlines()
                informacoes = [infor.split(" - ") for infor in informacoes]

                for linha in informacoes:
                    if int(linha[0]) == cod:
                        codigo_existe = True

            if codigo_existe:
                print(f"\n\n{'-' * 13}ERRO{'-' * 13}")

                print("CÓDIGO NUMÉRICO JÁ EXISTE!")

                print("-" * 30)

            else:
                descricao = str(input("Digite a descrição do produto: ")).strip()
                print("-" * 30)

                if descricao.strip() != "":
                    quantidade_atual = abs(int(input("Digite a quantidade atual do produto: ")))
                    print("-" * 30)

                    insercao.write(f"{cod} - {descricao} - {quantidade_atual}\n".encode("utf8"))

                    print(f"\n\n{'-' * 10}INFORMAÇÃO{'-' * 10}")

                    print("PRODUTO INSERIDO COM SUCESSO!")

                    print("-" * 30)

                else:
                    print(f"\n\n{'-' * 13}ERRO{'-' * 13}")

                    print("A DESCRIÇÃO NÃO PODE CONTER CARACTERES ESPECIAIS OU NÚMEROS!")

                    print("-" * 30)

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("ERRO AO RECEBER OS DADOS DO USUÁRIO OU AO LER O ARQUIVO!")
        print("-" * 30)

    except FileNotFoundError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 30)

    except OSError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 30)

    except IndexError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)

def deletar(arquivo):

    try:
        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as conteudo:
            informacoes = conteudo.read().decode("utf8").strip().splitlines()

            if len(informacoes) > 0:
                informacoes = [infor.split(" - ") for infor in informacoes]

                print(f"\n\n{'-' * 13}DELEÇÃ0{'-' * 13}")

                codigo = abs(int(input("Digite o código numérico do produto que você deseja deletar: ")))

                print("-" * 30)

                with open(arquivo, "wb") as delecao:
                    codigo_existe = False

                    for linha in informacoes:
                        if int(linha[0]) == codigo:
                            informacoes.remove(linha)
                            codigo_existe = True

                    for linha in informacoes:
                        delecao.write(f"{linha[0]} - {linha[1]} - {linha[2]}\n".encode("utf8"))

                    if codigo_existe:
                        print(f"\n\n{'-' * 10}INFORMAÇÃO{'-' * 13}")

                        print("PRODUTO DELETADO COM SUCESSO!")

                        print("-" * 30)

                    else:
                        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")

                        print("CÓDIGO NUMÉRICO NÃO EXISTENTE!")

                        print("-" * 30)

            else:
                print(f"\n\n{'-' * 13}ERRO{'-' * 13}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 30)

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 30)

    except FileNotFoundError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 30)

    except OSError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 30)

    except IndexError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)

def retirar(arquivo):

    try:
        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as leitura:
            informacoes = leitura.read().decode("utf8").strip().splitlines()

            if len(informacoes) > 0:
                informacoes = [infor.split(" - ") for infor in informacoes]
                print(f"\n\n{'-' * 13}RETIRADA{'-' * 13}")

                codigo = abs(int(input("Código numérico do produto que você deseja retirar: ")))

                print(f"{'-' * 30}")
                qtd_unidade = abs(int(input("Quantidade que você deseja retirar desse produto: ")))

                print("-" * 30)

                with open(arquivo, "wb") as remocao:
                    codigo_existe = False

                    for linha in range(len(informacoes)):
                        if int(informacoes[linha][0]) == codigo:
                            codigo_existe = True

                            if int(informacoes[linha][2]) > 0:
                                if (int(informacoes[linha][2]) - qtd_unidade) >= 0:
                                    informacoes[linha][2] = str(int(informacoes[linha][2]) - qtd_unidade)
                                    print(f"\n\n{'-' * 10}INFORMAÇÃO{'-' * 13}")

                                    print("UNIDADES RETIRADAS COM SUCESSO!")

                                    print("-" * 30)

                                else:
                                    print(f"\n\n{'-' * 13}ERRO{'-' * 13}")

                                    print("NÃO PODE RETIRAR UMA QUANTIDADE MAIOR DO QUE A DISPONÍVEL NO ESTOQUE!")

                                    print(f"{'-' * 30}")

                            else:
                                print(f"\n\n{'-' * 13}ERRO{'-' * 13}")

                                print("ACABOU O ESTOQUE DO PRODUTO INFORMADO!")

                                print(f"{'-' * 30}")

                    if not codigo_existe:
                        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")

                        print("CÓDIGO NUMÉRICO NÃO EXISTENTE!")

                        print("-" * 30)

                    for linha in informacoes:
                        remocao.write(f"{linha[0]} - {linha[1]} - {linha[2]}\n".encode("utf8"))

            else:
                print(f"\n\n{'-' * 13}ERRO{'-' * 13}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 30)

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 30)

    except FileNotFoundError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 30)

    except OSError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 30)

    except IndexError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)

def relatorio(arquivo):
  
    try:
        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as leitura:
            print(f"\n\n{'-' * 13}RELATÓRIO GERAL{'-' * 13}")

            texto = leitura.read().decode("utf-8").strip().splitlines()

            if len(texto) > 0:
                [print(f"{informacoes}\n{'-' * 30}") for informacoes in texto]

            else:

                print(f"\n{'-' * 30}")

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 30)

    except FileNotFoundError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 30)

    except OSError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 30)

def indisponiveis(arquivo):
 
    try:
        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as indisponivel:
            informacoes = indisponivel.read().decode("utf8").strip().splitlines()

            if len(informacoes) > 0:
                informacoes = [infor.split(" - ") for infor in informacoes]

                indisponivel = False

                print(f"\n\n{'-' * 12}PRODUTOS INDISPONIVÉIS{'-' * 12}")

                for linha in range(len(informacoes)):
                    if int(informacoes[linha][2]) > 0:
                        pass

                    else:
                        indisponivel = True
                        print(informacoes[linha][1])
                        print(f"{'-' * 30}")

                if not indisponivel:
                    print(f"\n{'-' * 30}")

            else:
                print(f"\n\n{'-' * 13}ERRO{'-' * 13}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 30)

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 30)

    except FileNotFoundError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 30)

    except OSError:
        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 30)

    except IndexError:
        print(f"\n{'-' * 30}")

        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)


if __name__ == "__main__":
    opcao = 0
    nome_arquivo = "arq.mercadorias.bin"

    try:
        while (opcao != 7 ):
            time.sleep(3)
            os.system('cls')
            print(f"\n\n{'-' * 13}MENU{'-' * 13}")
            print("1 - Inserir um produto")

            print(f"{'-' * 30}")
            print("2 - Deletar um produto")

            print(f"{'-' * 30}")
            print("3 - Remover unidades de produto")

            print(f"{'-' * 30}")
            print("4 - Relatório geral do arquivo")

            print(f"{'-' * 30}")
            print("5 - Produtos indisponivéis")

            print(f"{'-' * 30}")
            opcao = abs(int(input("\nDigite o número da opção que você deseja: ")))

            print(f"{'-' * 30}")

            if opcao == 1:
                inserir(nome_arquivo)

            elif opcao == 2:
                deletar(nome_arquivo)

            elif opcao == 3:
                retirar(nome_arquivo)

            elif opcao == 4:
                relatorio(nome_arquivo)

            elif opcao == 5:
                indisponiveis(nome_arquivo)

            else:
                print(f"\n\n{'-' * 10}FIM DO PROGRAMA{'-' * 10}")
                break

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("OPÇÃO INVÁLIDA!")
        print("-" * 30)


