'''
67. Faca uma funcao que receba duas strings e retorne a intercalacao letra a letra da primeira 
com a segunda string. A string intercalada deve ser retornada na primeira string.

'''

def intercalar(str1, str2):

    if type(str1) == str and type(str2) == str:
        inter = ''

        if len(str1) <= len(str2):
            for i in range(len(str1)):
                inter += str1[i] + str2[i]

        else:
            for i in range(len(str2)):
                inter += str1[i] + str2[i]

        return inter

if __name__ == '__main__':

    print("\nPrimeira palavras: ", end=" ")
    string1 = input()
    print("\nSegunda Palavra: ", end=" ")
    string2 = input()
    print(f"{intercalar(string1, string2)}")