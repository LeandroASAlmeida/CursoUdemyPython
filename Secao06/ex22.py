'''Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
uma sequencia arbitraria de notas (validas no intervalo de 10 a 20) e que mostre na tela, 
como resultado, a correspondente media aritmetica. O numero de notas com que o aluno
pretenda efetuar o calculo nao ser a fornecido ao programa, o qual terminar a quando for 
introduzido um valor que nao seja valido como nota de aprovacao.'''

nota = int(input("Insira uma nota de 10 a 20: "))
media = 0
qtd = 0  # quantidade de valores inseridos

while nota < 10 or nota > 20:
    print('NOTA INVALIDA')
    nota = int(input("Insira uma nota de 10 a 20: "))

while nota >= 10 and nota <= 20:
    media = media + nota
    qtd = qtd + 1
    nota = int(input("Insira uma nota de 10 a 20: "))

print(f"A média aritmética entre os valores inseridos é {media / qtd}.")