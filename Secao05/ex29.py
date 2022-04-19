''' Faca uma prova de matematica para criancas que estao aprendendo a somar numeros 
inteiros menores do que 100. Escolha numeros aleatorios entre 1 e 100, e mostre na 
tela a pergunta: qual e a soma de a + b, onde a e b sao os numeros aleatorios. Peca a 
resposta. Faca cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, alem de quantas vezes o aluno acertou'''

from random import randint

c = 0
for contador in range(1, 6):
    a = randint(1, 100)
    b = randint(1, 100)
    conta = int(input(f'{contador}- Qual o valor da soma de {a} + {b}? ='))
    resul = a + b
    if conta == resul:
        print('Acertou ^^')
        c += 1
    else:
        print('Infelizmente você errou.')
print(f'Você acertou {c} questões.')
