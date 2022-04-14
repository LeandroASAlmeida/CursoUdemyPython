""" Operadores unarios:
        .not
    Operadores binários:
        .and, or , is

Regras de funcionamento:
Para o  'and', ambos os valores precisam ser True
Para o 'or' ,um ou outro valor precisa ser True
Para o 'not' o valor do booleano é invertido,ou seja, se for True, via False, se for False vira True
Para o 'is', o valor é comparado com o segundo

"""

ativo = True
logado= True

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo  usuário')

print(not False)


"""if ativo and logado: # SE O ATIVO FOR VERDADEIRO "E" LOGADO  TAMBEM. - IRÁ FUNCIONAR
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')"""

