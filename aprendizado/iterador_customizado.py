"""
Escrevendo um iterador customizado

"""


class Contador: # classe de dados
    def __init__(self, menor, maior): # função dentro de uma classe chamasse 'Metodo' / __init__= construtor = criar objetos / self aparece dentro de um metodo.
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration # A palavra-chave raise gera um erro e interrompe o fluxo de controle do programa. Ele é usado para trazer a exceção atual em um manipulador de exceção para que ela possa ser tratada mais adiante na pilha de chamadas


for n in Contador(1, 61):
    print(n)


for n in range(1, 61):
    print(n)

