'''
61. Crie uma funcao que calcula o comprimento de uma string e que possui a seguinte 
assinatura: void tamanho(char *str, int *strsize).

'''
def tam(a):
   if type(a) == str:
        cont = 0

        for _ in a:
            cont += 1

        return cont
if __name__ == '__main__':

    print("Informe uma palavra: ", end=" ")
    pal = input()
    print(f"O comprimento de '{pal}': {tam(pal)}")