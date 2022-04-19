'''Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preco antigo,
calcule e escreva o preco novo, e escreva uma mensagem em funcao do preco novo (de 
acordo com a segunda tabela).'''


valorAntigo = float(input('Qual o valor Antigo?'))

if valorAntigo < 50:
    valorNovo = valorAntigo + ((valorAntigo / 100) * 5)
    print(f'Esse produto custa agora {valorNovo:.2f}')
    if valorNovo < 80:
        print('Esse produto está barato')
    elif 80 < valorNovo < 120:
        print('Esse produto está normal')
    elif 120 < valorNovo < 200:
        print('Esse produto está caro')
    elif 200 < valorNovo:
        print('Esse produto está muito caro')
if 50 < valorAntigo < 100:
    valorNovo = valorAntigo + ((valorAntigo / 100) * 10)
    print(f'Esse produto custa agora {valorNovo:.2f}')
    if valorNovo < 80:
        print('Esse produto está barato')
    elif 80 < valorNovo < 120:
        print('Esse produto está normal')
    elif 120 < valorNovo < 200:
        print('Esse produto está caro')
    elif 200 < valorNovo:
        print('Esse produto está muito caro')
if valorAntigo > 100:
    valorNovo = valorAntigo + ((valorAntigo / 100) * 15)
    print(f'Esse produto custa agora {valorNovo:.2f}')
    if valorNovo < 80:
        print('Esse produto está barato')
    elif 80 < valorNovo < 120:
        print('Esse produto está normal')
    elif 120 < valorNovo < 200:
        print('Esse produto está caro')
    elif 200 < valorNovo:
        print('Esse produto está muito caro')