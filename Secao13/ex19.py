"""
19. Faça um programa que receba do usuário um arquivo que contenha o nome e a nota de
diversos alunos (da seguinte forma: NOME: JOÃO NOTA: 8), um aluno por linha. Mostre na tela o nome e a nota do aluno que possui a maior nota.

"""
nome_arquivo = str(input("Digite o caminho do arquivo : "))#arquivos\notas.alunos.txt


with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        # strip() para remover os espaçoes e as quebras de linhas desnecessárias
        # do início e final do arquivo. splitlines() para criar um vetor
        # onde cada elemento é uma linha do arquivo
    linhas = arquivo.read().lower().strip().splitlines()

        # Removendo as partes do texto que contém "nome:" e "nota:"
    linhas = [linha.replace("nome:", "") for linha in linhas]
    linhas = [linha.replace("nota:", "") for linha in linhas]

    linhas = [linha.split() for linha in linhas]

        # Pegando o vetor que contém as informações do aluno com a maior nota
    aluno = max((linha for linha in linhas), key=lambda dados: float(dados[-1])) # consiste em uma função que é atribuida a um objeto. Por conter a palavra reservada lambda o objeto se comportará como uma função

    nome = aluno[0]
    nota = float(aluno[-1])

    print(f"\n{nome.title()} - {nota}") # O title()método retorna uma string onde o primeiro caractere em cada palavra é maiúsculo

