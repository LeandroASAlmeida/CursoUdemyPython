"""
29. Codifique um programa que manipule um arquivo contendo registros descritos pelos se
guintes campos: codigo vendedor, nome vendedor, valor da venda e mes.
A manipulação do arquivo em questão é feita através da execução das operações disponibilizadas pelo seguinte menu:
• Criar o arquivo de dados; 
• Incluir um determinado registro no arquivo; 
• Excluir um determinado vendedor no arquivo; 
• Alterar o valor de uma venda no arquivo; 
• Imprimir os registros na saída padrão; 
• Excluir o arquivo de dados;
. Finalizar o programa. Os registros devem estar ordenados no arquivo, de forma crescente,
 de acordo com as informações contidas nos campos codigo vendedor e mes. 
 Não deve existir mais de um registro no arquivo com mesmos valores nos campos codigo vendedor e mês.

"""
import os
import time
from os import path # caminho local
from os import remove # os.remove()O método em Python é usado para remover ou excluir um caminho de arquivo

def verificar_nome(nome):
    """Função que recebe um nome e verifica se o mesmo é válido ou não.
    Caso o nome seja válido retorna True, caso contrário retorna False"""

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

def criar_arquivo(arquivo):

    try:
        with open(arquivo, "a") as _:
            pass

        print(f"\n\n{'-' * 10}INFORMAÇÕES{'-' * 11}")
        print("ARQUIVO CRIADO COM SUCESSO!")
        print("-" * 30)

    except FileNotFoundError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 30)

    except OSError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 30)

def inserir_registro(arquivo):

    try:
        arquivo_existe = path.exists(arquivo)

        if arquivo_existe:
            print(f"\n\n{'-' * 13}INSERIR{'-' * 14}")

            codigo_vendedor = abs(int(input("Insira o código do vendedor: ")))
            print(f"{'-' * 30}")

            nome_vendedor = str(input("Insira o nome do vendedor: ")).strip().title()
            print(f"{'-' * 30}")

            if verificar_nome(nome_vendedor):
                valor_venda = abs(float(input("Insira o valor da venda: ")))
                print(f"{'-' * 30}")

                mes = abs(int(input("Insira o número referente ao mês da venda: ")))
                print(f"{'-' * 30}")

                if (mes >= 1) and (mes <= 12):
                    existe = False

                    with open(arquivo, "r", encoding="utf-8") as verificacao:
                        texto = verificacao.read().strip().splitlines()

                        texto = [informacoes.split(";") for informacoes in texto]

                        for linha in texto:
                            if codigo_vendedor == int(linha[0]) and mes == int(linha[3]):
                                existe = True

                    if not existe:
                        with open(arquivo, "a", encoding="utf-8") as insercao:
                            insercao.write(f"{codigo_vendedor};{nome_vendedor};{valor_venda};{mes}\n")

                        print(f"\n\n{'-' * 10}INFORMAÇÕES{'-' * 11}")
                        print("REGISTRO INSERIDOS COM SUCESSO!")
                        print("-" * 30)

                    else:
                        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
                        print("EXISTE UM REGISTRO COM OS MESMOS VALORES NO CÓDIGO DO VENDEDOR E MÊS DA VENDA!")
                        print("-" * 30)

                else:
                    print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
                    print("MÊS INVÁLIDO!")
                    print("-" * 30)

            else:
                print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
                print("O NOME DO VENDEDOR NÃO PODE CONTER CARACTERES ESPECIAIS OU NÚMEROS!")
                print("-" * 30)

        else:
            print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
            print("O ARQUIVO NÃO EXISTE. PRIMEIRO CRIE O ARQUIVO!")
            print("-" * 30)

    except ValueError:
        print(f"{'-' * 30}")

        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("ERRO AO RECEBER OS DADOS DO USUÁRIO!")
        print("-" * 30)

    except IndexError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)

def excluir_vendedor(arquivo):
  
    try:
        arquivo_existe = path.exists(arquivo)

        if arquivo_existe:
            print(f"\n\n{'-' * 11}EXCLUIR{'-' * 11}")

            codigo_vendedor = abs(int(input("Insira o código do vendedor: ")))
            print(f"{'-' * 30}")

            with open(arquivo, "r", encoding="utf-8") as leitura:
                texto = leitura.read().strip().splitlines()

                texto = [informacoes.split(";") for informacoes in texto]

                conteudo = ""
                existe = False

                for linha in texto:
                    if codigo_vendedor == int(linha[0]):
                        existe = True

                    else:
                        cod, nome, venda, mes = linha[0], linha[1], linha[2], linha[3]

                        conteudo += f"{cod};{nome};{venda};{mes}\n"

                if existe:
                    with open(arquivo, "w", encoding="utf-8") as deletando:
                        deletando.write(conteudo)

                        print(f"\n\n{'-' * 10}INFORMAÇÕES{'-' * 10}")
                        print("VENDEDOR DELETADO COM SUCESSO!")
                        print("-" * 30)

                else:
                    print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
                    print("O CÓDIGO DO VENDEDOR INFORMADO NÃO EXISTE!")
                    print("-" * 30)

        else:
            print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
            print("O ARQUIVO NÃO EXISTE. PRIMEIRO CRIE O ARQUIVO!")
            print("-" * 30)

    except ValueError:
        print(f"{'-' * 30}")

        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("ERRO AO RECEBER OS DADOS DO USUÁRIO!")
        print("-" * 30)

    except IndexError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)

def alterar_venda(arquivo):
 
    try:
        arquivo_existe = path.exists(arquivo)

        if arquivo_existe:
            print(f"\n\n{'-' * 10}ALTERAR VALOR{'-' * 11}")

            codigo_vendedor = abs(int(input("Insira o código do vendedor: ")))
            print(f"{'-' * 30}")

            cod_existe = False

            with open(arquivo, "r", encoding="utf-8") as verificacao:
                texto = verificacao.read().strip().splitlines()

                texto = [informacoes.split(";") for informacoes in texto]

                for linha in texto:
                    if codigo_vendedor == int(linha[0]):
                        cod_existe = True

                if cod_existe:
                    mes_venda = abs(int(input("Insira o número referente ao mês da venda: ")))
                    print(f"{'-' * 30}")

                    if (mes_venda >= 1) and (mes_venda <= 12):
                        mes_existe = False

                        for linha in texto:
                            if mes_venda == int(linha[3]):
                                mes_existe = True

                        if mes_existe:
                            novo_valor = abs(float(input("Insira o novo valor da venda: ")))
                            print(f"{'-' * 30}")

                            conteudo = ""

                            for linha in texto:
                                cod, nome, valor, mes = int(linha[0]), linha[1], float(linha[2]), int(linha[3])

                                if (codigo_vendedor == cod) and (mes_venda == mes):
                                    conteudo += f"{cod};{nome};{novo_valor};{mes}\n"

                                else:
                                    conteudo += f"{cod};{nome};{valor};{mes}\n"

                            with open(arquivo, "w", encoding="utf-8") as alterando:
                                alterando.write(conteudo)

                                print(f"\n\n{'-' * 10}INFORMAÇÕES{'-' * 11}")
                                print("VALOR ALTERADO COM SUCESSO!")
                                print("-" * 30)

                        else:
                            print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
                            print("O MÊS DA VENDA INFORMADO NÃO EXISTE!")
                            print("-" * 30)

                    else:
                        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
                        print("MÊS INVÁLIDO!")
                        print("-" * 30)

                else:
                    print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
                    print("CÓDIGO NÃO EXISTE!")
                    print("-" * 30)

        else:
            print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
            print("O ARQUIVO NÃO EXISTE. PRIMEIRO CRIE O ARQUIVO!")
            print("-" * 30)

    except ValueError:
        print(f"{'-' * 30}")

        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("ERRO AO RECEBER OS DADOS DO USUÁRIO!")
        print("-" * 30)

    except IndexError:
        print(f"\n\n{'-' * 14}ERRO{'-' * 15}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)

def imprimir_registros(arquivo):
    
    try:
        arquivo_existe = path.exists(arquivo)

        if arquivo_existe:
            with open(arquivo, "r", encoding="utf-8") as leitura:
                print(f"\n\n{'-' * 11}REGISTRO{'-' * 12}")
                texto = leitura.read().strip().splitlines()

                if len(texto) > 0:
                    [print(f"{informacao.replace(';', ' - ')}\n{'-' * 30}") for informacao in texto]

                else:
                    print(f"\n{'-' * 30}")

        else:
            print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
            print("O ARQUIVO NÃO EXISTE. PRIMEIRO CRIE O ARQUIVO!")
            print("-" * 30)

    except IndexError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)

def excluir_arquivo(arquivo):
   
    try:
        arquivo_existe = path.exists(arquivo)

        if arquivo_existe:
            remove(arquivo)

            print(f"\n\n{'-' * 10}INFORMAÇÕES{'-' * 10}")
            print("ARQUIVO EXCLUÍDO COM SUCESSO!")
            print("-" * 30)

        else:
            print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
            print("O ARQUIVO NÃO EXISTE. PRIMEIRO CRIE O ARQUIVO!")
            print("-" * 30)

    except IndexError:
        print(f"\n\n{'-' * 10}ERRO{'-' * 11}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 30)


if __name__ == "__main__":
    opcao = 0
    nome_arquivo = "arq.vendedores.txt"

    try:
        while (opcao != 7 ):
            time.sleep(3)
            os.system('cls')
            print(f"\n\n{'+' * 14}MENU{'+' * 13}")
            print("1 - Criar o arquivo de dados")
            print(f"{'-' * 30}")

            print("2 - Incluir registro no arquivo")
            print(f"{'-' * 30}")

            print("3 - Excluir vendedor no arquivo")
            print(f"{'-' * 30}")

            print("4 - Alterar o valor de uma venda ")
            print(f"{'-' * 30}")

            print("5 - Imprimir os registros ")
            print(f"{'-' * 30}")

            print("6 - Excluir o arquivo de dados")
            print(f"{'-' * 30}")

            print("7 - Finalizar o programa")
            print(f"{'-' * 30}")

            opcao = abs(int(input("\nDigite o número da opção que você deseja: ")))

            print(f"{'-' * 30}")

            if opcao == 1:
                criar_arquivo(nome_arquivo)

            elif opcao == 2:
                inserir_registro(nome_arquivo)

            elif opcao == 3:
                excluir_vendedor(nome_arquivo)

            elif opcao == 4:
                alterar_venda(nome_arquivo)

            elif opcao == 5:
                imprimir_registros(nome_arquivo)

            elif opcao == 6:
                excluir_arquivo(nome_arquivo)

            elif opcao == 7:
                print(f"\n\n{'-' * 12}FIM DO PROGRAMA{'-' * 13}")
                break

    except ValueError:
        print("-" * 30)

        print(f"\n\n{'-' * 13}ERRO{'-' * 13}")
        print("OPÇÃO INVÁLIDA!")
        print("-" * 30)

