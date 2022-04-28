'''2. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
elementos. Escreva ao final a matriz obtida'''


l=int()
c=int()
matriz=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


for l in range(0,5):
    for c in range(0,5):
        if (l == c):
            matriz[l][c] = 1
        print(f'[{matriz[l][c]:^5}]', end ='')

    print()



















'''
int main()
{
    int matriz[5][5];
  
     //PREENCHIMENTO DA MATRIZ
    for(int linha = 0 ; linha < 5; linha++)
    {
        for(int coluna = 0 ; coluna < 5; coluna++)
        {
            if(linha == coluna) matriz[linha][coluna] = 1 ; //Diagonal principal
            else matriz[linha][coluna] = 0;
        }
     }'''


