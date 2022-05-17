"""
Crie uma classe para representar uma pessoa, como os atirbutos privados de
nome, idade e altura. Crie os métodos públicos necessários para sets e gets e
também um método para imprimir os dados de uma pessoa.
"""

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade
        
    def setAltura(self, altura):
        self.altura = altura

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade
        
    def getAltura(self):
        return self.altura

    def imprimi_nome(self):
        print(self.nome)

    def imprimi_idade(self):
        print(self.idade)

    def imprimir_altura(self):
        print(self.altura)

    def imprimir_tudo(self):
        return f'{self.nome},{self.idade},{self.altura}'

person1 = Pessoa('Leandro', 34, 1.84)
person2 = Pessoa('João', 15, 1.65)
person3 = Pessoa("Pedro Henrique Gomes Lima", 21, 1.70)
person4 = Pessoa("Áquila Rodrigues Menezes", 23, 1.75)
person5 = Pessoa("Marcos Vitor Bezerra", 29, 1.85)
person6 = Pessoa("Rian Marlon Sousa da Silva", 25, 1.76)
person7 = Pessoa("Vitor Emanuel Sampaio Cavalcante", 29, 1.80)
person8 = Pessoa("Raffa Muela Mano", 49, 1.90)


print (person1.imprimir_tudo())
print (person2.imprimir_tudo())
print (person3.imprimir_tudo())
print (person4.imprimir_tudo())
print (person5.imprimir_tudo())
print (person6.imprimir_tudo())
print (person7.imprimir_tudo())
print (person8.imprimir_tudo())



