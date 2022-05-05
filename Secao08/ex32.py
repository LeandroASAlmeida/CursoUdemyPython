'''
32. Faca uma funcao chamada ‘simplifica’ que recebe como parametro o num e o de- 
nominador de uma fracao. Esta funcao deve simplificar a fracao recebida dividindo o 
num e o deno pelo maior fator possıvel. Por exemplo, a fracao 36/60 sim- 
plifica para 3/5 dividindo o num e o deno por 12. A funcao deve modificar 
as variaveis passadas como parametro.

'''

def simplifica(num,deno):

    if deno > 0:
        for i in range(deno, 1, -1):
            if num % i == 0 and deno % i == 0:
                num = int(num / i)
                deno = int(deno / i)

                break

    else:

        for i in range(deno*(-1), 1, -1):
            if num % i == 0 and deno % i == 0:
                num = int(num / i)
                deno = int(deno / i)

                break

    return num, deno


num1 = int(input("Digite o num da fração: "))
deno1 = int(input("Digite o deno da fração: "))

novo_num, novo_deno = simplifica(num1, deno1)

print(f"\nFração simplificada: {novo_num} / {novo_deno}")