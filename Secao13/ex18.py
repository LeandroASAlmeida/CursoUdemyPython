"""
18. Faça um programa que leia um arquivo contendo o nome e o preço de diversos produtos
(separados por linha), e calcule o total da compra.
"""


def verificar_nome(nome):

    caracteres_invalidos = ["-", ":", "?", "/", ">", "<", "}", "{", "[", "]",
                            "+", "*", "@", "!", "%", "¨", ";", "´", "`", "^", "~",
                            "=", "(", ")", "&", "_", "$", "#", ","]


    for caractere in nome:
        if str(caractere).isnumeric() or str(caractere) in caracteres_invalidos:
            return False

    return True

   
lista = int(input("Digite a quantidade de produtos: ")) 

nome_produtos = []
preco_produtos = []
total = 0

for produto in range(lista):

    while True:
        nome = str(input(f"\nDigite o nome do produto {produto+1}: ")).strip().title()

        if verificar_nome(nome):
              
            novo_nome = nome[0:30:1] if len(nome) >= 30 else nome + " " * (30 - len(nome))
            preco = abs(float(input(f"Digite o preço do produto {nome}: ")))

            nome_produtos.append(novo_nome)
            preco_produtos.append(preco)

        
        break

with open("arquivos/listacompras.txt", "a", encoding="utf-8") as arquivo:
    for i in range(lista):
        arquivo.write(f"{nome_produtos[i]} {preco_produtos[i]}\n")


    print("\nInformações inseridas no arquivo com sucesso!")
    total = sum(preco_produtos)
    print(f'O valor total da lista é de {total} ')

