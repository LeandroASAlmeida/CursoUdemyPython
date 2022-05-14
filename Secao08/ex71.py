
'''71 -Considerando a estrutura:
    struct Ponto{
    int x;
    int y;
    };
Para representar um ponto em uma grade 2D, implemente uma função que indique se um
ponto p está localicado dentro ou fora de um retângulo. O retângulo é definico
por seus vértices inferior esquerdo v1 e superior direito v2. A função deve retornar
1 caso o ponto esteja localizado dentro do retângulo e 0 caso contrário. Essa função deve
obedecer ao protótipo:
int dentroRet (struct Ponto* v1, struct Ponto* v2, struct Ponto* p);
'''



def dentro_ret(x1, y1, x2, y2, p1, p2):

    if (x1 <= p1) and (x2 >= p1):
        if (y1 <= p2) and (y2 >= p2):
            return 1

    return 0


x1 = int(input("Coordenada x do vértice inferior esquerdo do retângulo: "))
y1 = int(input("Coordenada y do vértice inferior esquerdo do retângulo: "))
x2 = int(input("\nCoordenada x do vértice superior direita do retângulo: "))
y2 = int(input("coordenada y do vértice superior direita do retângulo: "))

p1 = int(input("\nCoordenada x do ponto: "))
p2 = int(input("Coordenada y do ponto: "))

print(f"\n{dentro_ret(x1, y1, x2, y2, p1, p2)}")