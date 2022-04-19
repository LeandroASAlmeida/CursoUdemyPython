'''Uma empresa decide dar um aumento aos seus funcionarios de acordo com uma tabela 
que considera o salario atual e o tempo de servico de cada funcionario. Os funcionarios 
com menor salario terao um aumento proporcionalmente maior do que os funcionarios 
com um salario maior, e conforme o tempo de servico na empresa, cada funcionario ir  a
receber um bonus adicional de salario. Faca um programa que leia:'''


tempo = int(input("A quantos anos você trabalha na empresa? "))
salario = float(input("Qual o valor de seu salário em reais? "))

if salario < 500:
    if tempo < 1:
        print(f"Seu novo salário será de R${salario * 1.25}")
    elif 1 <= tempo <= 3:
        print(f"Seu novo salário será de R${salario * 1.25 + 100}")
    elif 4 <= tempo <= 6:
        print(f"Seu novo salário será de R${salario * 1.25 + 200}")
    elif 7 <= tempo <= 10:
        print(f"Seu novo salário será de R${salario * 1.25 + 300}")
    elif tempo > 10:
        print(f"Seu novo salário será de R${salario * 1.25 + 500}")
elif 500 <= salario < 1000:
    if tempo < 1:
        print(f"Seu novo salário será de R${salario * 1.20}")
    elif 1 <= tempo <= 3:
        print(f"Seu novo salário será de R${salario * 1.20 + 100}")
    elif 4 <= tempo <= 6:
        print(f"Seu novo salário será de R${salario * 1.20 + 200}")
    elif 7 <= tempo <= 10:
        print(f"Seu novo salário será de R${salario * 1.20 + 300}")
    elif tempo > 10:
        print(f"Seu novo salário será de R${salario * 1.20 + 500}")
elif 1000 <= salario < 1500:
    if tempo < 1:
        print(f"Seu novo salário será de R${salario * 1.15}")
    elif 1 <= tempo <= 3:
        print(f"Seu novo salário será de R${salario * 1.15 + 100}")
    elif 4 <= tempo <= 6:
        print(f"Seu novo salário será de R${salario * 1.15 + 200}")
    elif 7 <= tempo <= 10:
        print(f"Seu novo salário será de R${salario * 1.15 + 300}")
    elif tempo > 10:
        print(f"Seu novo salário será de R${salario * 1.15 + 500}")
elif 1500 <= salario <= 2000:
    if tempo < 1:
        print(f"Seu novo salário será de R${salario * 1.10}")
    elif 1 <= tempo <= 3:
        print(f"Seu novo salário será de R${salario * 1.1 + 100}")
    elif 4 <= tempo <= 6:
        print(f"Seu novo salário será de R${salario * 1.10 + 200}")
    elif 7 <= tempo <= 10:
        print(f"Seu novo salário será de R${salario * 1.10 + 300}")
    elif tempo > 10:
        print(f"Seu novo salário será de R${salario * 1.10 + 500}")
elif salario > 2000:
    if tempo < 1:
        print(f"Seu novo salário será de R${salario}")
    elif 1 <= tempo <= 3:
        print(f"Seu novo salário será de R${salario + 100}")
    elif 4 <= tempo <= 6:
        print(f"Seu novo salário será de R${salario + 200}")
    elif 7 <= tempo <= 10:
        print(f"Seu novo salário será de R${salario + 300}")
    elif tempo > 10:
        print(f"Seu novo salário será de R${salario + 500}")