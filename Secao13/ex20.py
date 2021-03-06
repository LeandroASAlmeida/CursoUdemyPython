"""
20. Crie um programa que receba como entrada o número de alunos de uma disciplina.
Aloque dinamicamente dois vetores para armazenar as informações a respeito desses alunos. 
O primeiro vetor contém o nome dos alunos e o segundo contém suas notas finais. 
Crie um arquivo que armazene, a cada linha, o nome do aluno e sua nota final. Use nomes
com no máximo 40 caracteres. Se o nome não contém 40 caracteres, complete com espaço em branco.

"""

def verificar_nome(nome):

    caracteres_invalidos = ["-", ":", "?", "/", ">", "<", "}", "{", "[", "]",
                            "+", "*", "@", "!", "%", "¨", ";", "´", "`", "^", "~",
                            "=", "(", ")", "&", "_", "$", "#", ","]


    for caractere in nome:
        if str(caractere).isnumeric() or str(caractere) in caracteres_invalidos:
            return False

    return True

   
qtd_alunos = int(input("Digite a quantidade de alunos: ")) # receba como entrada o número de alunos

nome_alunos = [] # Aloque dinamicamente dois vetores para armazenar as informações
nota_alunos = []#O primeiro vetor contém o nome dos alunos e o segundo contém suas notas finais. 

for aluno in range(qtd_alunos):

    while True:
        nome = str(input(f"\nDigite o nome do aluno {aluno+1}: ")).strip().title()

        if verificar_nome(nome):
            novo_nome = nome[0:40:1] if len(nome) >= 40 else nome + " " * (40 - len(nome))
            nota = abs(float(input(f"Digite a nota final do {nome}: ")))

            nome_alunos.append(novo_nome)
            nota_alunos.append(nota)

            break

        else:
            print("\nNome inválido!")

with open("arquivos/alunos_notas.txt", "a", encoding="utf-8") as arquivo: # Crie um arquivo que armazene, a cada linha, o nome do aluno e sua nota final.
    for i in range(qtd_alunos):
        arquivo.write(f"{nome_alunos[i]} {nota_alunos[i]}\n")

print("\nInformações inseridas no arquivo com sucesso!")

