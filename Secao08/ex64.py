'''
63. Implemente a funcao a qual recebe duas strings, str1 e str2, e concatena a string apontada por str2 a string apontada por ` str1.

'''

def palavra(str1, str2):
    x = str1 + " " + str2
    y = str2 + " " + str1
    return [x,y]

if __name__ == '__main__':

    print("Informe a primeira palavra: ",end=" ")
    a = input()
    print("\nInforme a segunda palavra: ", end=" ")
    b = input()
    print(f"\nString1 : {palavra(a,b)[0]}")
    print(f"\nString2 : {palavra(a,b)[1]}")