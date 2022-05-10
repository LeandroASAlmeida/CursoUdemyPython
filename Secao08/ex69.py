'''Faça um programa que faça operações simples de frações:
 - Crie a leia duas frações p e q, compostas por numerador e denominador.

 -encontre o maximo divisor comum entre o denominador e simplifique as frações.

 -Apresente a soma, a subtração, o produto e o quociente entre as frações lidas

 Obs: Criar uma função para cada item.
'''
def cria_fracao():


    numerador_p = int(input("Digite o numerador da primeira fração: "))
    denominador_p = int(input("Digite o denominador da primeira fração: "))

    numerador_q = int(input("\nDigite o numerador da segunda fração: "))
    denominador_q = int(input("Digite o denominador da segunda fração: "))
    print()

    return numerador_p, denominador_p, numerador_q, denominador_q


def simplifica_fracao(numerador_p, denominador_p):
 

    if denominador_p > 0:
        for i in range(denominador_p, 0, -1):
            if numerador_p % i == 0 and denominador_p % i == 0:
                print(f"Fração {numerador_p} / {denominador_p} simplificada: "
                      f"{int(numerador_p / i)} / {int(denominador_p / i)}")
                break

    elif denominador_p < 0:
        for i in range(denominador_p, 0, 1):
            if numerador_p % i == 0 and denominador_p % i == 0:
                print(f"Fração {numerador_p} / {denominador_p} simplificada: "
                      f"{int(numerador_p / i)} / {int(denominador_p / i)}")
                break


def calculo_fracoes(numerador_p, denominador_p, numerador_q, denominador_q):


    if denominador_p == denominador_q:
        novo_num = numerador_p + numerador_q
        novo_deno = denominador_p

        print(f"\nA soma das duas frações: {novo_num} / {novo_deno}")
        simplifica_fracao(novo_num, novo_deno)

        novo_num = numerador_p - numerador_q
        novo_deno = denominador_p
        print(f"\nA subtração das duas frações: {novo_num} / {novo_deno}")
        simplifica_fracao(novo_num, novo_deno)

    elif denominador_p != denominador_q:

        mmc = 1
        dividindo1 = int(denominador_p)
        dividindo2 = int(denominador_q)

        for i in range(denominador_p):

            for j in range(2, (denominador_p+denominador_q)):
                if dividindo1 % j == 0 and dividindo2 % j == 0:
                    dividindo1 = int(dividindo1 / j)
                    dividindo2 = int(dividindo2 / j)

                    mmc *= j
                    break

                elif dividindo1 % j == 0 and not(dividindo2 % j == 0):
                    dividindo1 = int(dividindo1 / j)

                    mmc *= j
                    break

                elif dividindo2 % j == 0 and not(dividindo1 % j == 0):
                    dividindo2 = int(dividindo2 / j)

                    mmc *= j
                    break

            if dividindo1 == 1 and dividindo2 == 1:
                break

        nume1 = int(mmc / denominador_p * numerador_p)
        nume2 = int(mmc / denominador_q * numerador_q)

        novo_num = nume1 + nume2

        print(f"\nA soma das duas frações: {novo_num} / {mmc}")
        simplifica_fracao(novo_num, mmc)

        novo_num = nume1 - nume2
        print(f"\nA subtração das duas frações: {novo_num} / {mmc}")
        simplifica_fracao(novo_num, mmc)

    novo_num = numerador_p * numerador_q
    novo_deno = denominador_p * denominador_q
    print(f"\nO produto das duas frações: {novo_num} / {novo_deno}")
    simplifica_fracao(novo_num, novo_deno)

    novo_num = numerador_p * denominador_q
    novo_deno = denominador_p * numerador_q
    print(f"\nO quociente das duas frações: {novo_num} / {novo_deno}")
    simplifica_fracao(novo_num, novo_deno)


numerador_p, den1, numerador_q, den2 = cria_fracao()
simplifica_fracao(numerador_p, den1)
simplifica_fracao(numerador_q, den2)
calculo_fracoes(numerador_p, den1, numerador_q, den2)

