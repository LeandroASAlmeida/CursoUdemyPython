'''
11. Elabore uma funcao que receba tres notas de um aluno como parametros e uma letra. 
Se a letra for A, a funcao devera calcular a media aritmetica das notas do aluno; se for P, 
devera calcular a media ponderada, com pesos 5, 3 e 2.

'''

def nota(l, *args):
    if l == "p" or l == "P": # se for P devera calcular a media ponderada,
        return ((args[0] * 5) + (args[1] * 3) + (args[2] * 2)) / (5+3+2)
    
    elif l == "a" or l == "A": # Se a letra for A, a funcao devera calcular a media aritmetica das notas do aluno
        return sum(args) / 3
    else:
        return f"{l} invalido."

notas = []
for i in range(0,4):
    print(f"Informe a {i}° nota: ", end=" ")
    n = float(input())
    notas.append(n)
print("""\n
 Informe o tipo de media:
 P -> Media Ponderada
 A -> Media Aritmética
 Media: """, end=" ")
op = input()
print(f"\nNota: {nota(op, *notas)}")
