
'''
72) Considerando a estrutura
    struct Vetor{
    float x;
    float y;
    float z;
    };
para representar um vetor de R³, implemente umaa função que calcule a soma
de dois vetores. Essa função deve obedecer ao protótipo:
void soma (struct Vetor* v1, struct Vetor* v2, struct Vetor* res);
onde os parâmetros v1 e v2 são ponteiros para os vetores a seren somados, e o parâmetro
res é um ponteiro para uma estrutura vetor onde o resultado da operação deve ser
armazenado
'''


def soma(v1, v2):

    elementos = True

    for i in v1:
        if not(type(i) == int or type(i) == float):
            elementos = False

    for i in v2:
        if not(type(i) == int or type(i) == float):
            elementos = False

    if elementos:
        novo_vetor = []

        if len(v1) >= len(v2):
            for i in range(len(v2)):
                novo_vetor.append(v1[i] + v2[i])

            for i in range(len(novo_vetor), len(v1)):
                novo_vetor.append(v1[i])

        elif len(v2) > len(v1):
            for i in range(len(v1)):
                novo_vetor.append(v1[i] + v2[i])

            for i in range(len(novo_vetor), len(v2)):
                novo_vetor.append(v2[i])

        return novo_vetor

if __name__ == '__main__':

    vetor1 = []
    vetor2 = []

    for i in range(0,9):
        vetor1.append(int(input('Digite um número : ')))
    print('-=' * 30) # linha de separação
    for i in range(0,5):
        vetor2.append(int(input('Digite outro número : ')))



print(f"Soma dos vetores: {soma(vetor1, vetor2)}")

