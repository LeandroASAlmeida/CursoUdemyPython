'''
1) Escreva um programa que:
    (a) Crie/abra um arquivo texto de nome "arq.txt"
    (b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário
    entre com o caractere '0'
    (c) Feche o arquivo
Agora, abra e leia o arquivo, caractere por caractere, escreva na tela todos os caracteres
armazenados
'''

with open('arquivos/arq.txt', 'a', encoding='utf-8') as arq: # 'a'  - aberto para escrita, anexando ao final do arquivo se existir
    while True:
        texto = str(input("Digite um texto (0, caso queira sair): ")).strip().capitalize() # remove aspas  / primeira letra da frase sempre maiscula
        if texto != '0':
                arq.write(texto+"\n")

        else:
            break














