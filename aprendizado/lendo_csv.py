from csv import reader
from csv import DictReader
from encodings import utf_8


with open("lutadores.csv", encoding="utf-8") as arquivo:
    dados = arquivo.read()
    print(type(dados))
    dados = dados.split(',')
    print(dados)

'''with open("lutadores.csv", 'r') as arq:
    csvreader = csv.reader(arq)
    for row in csvreader:
        rows.append(row)
print(rows)'''

with open("lutadores.csv", encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # pula o cabecalho
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centimetros')

with open("lutadores.csv" , encoding='utf_8')  as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")