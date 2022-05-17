'''def cabecalho(texto,alinhamento = True): #Função para gerar cabecalho de programa
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50,'#')
    
print(cabecalho('geek university')) #Geek University
                                    #---------------


print(cabecalho('geek university', alinhamento= False)) # #################Geek University##################


def cabecalho(texto: str,alinhamento: bool = True)-> str: #Função para gerar cabecalho de programa
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50,'#')
    
print(cabecalho('geek university')) #Geek University
                                    #---------------


print(cabecalho('geek university', alinhamento= False)) # #################Geek University##################
'''
cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)
print(cesta)