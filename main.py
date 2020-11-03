# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np

def nbrDeVariable():
    temp = input("Entrez les noms de vos variables en les séparants par une virgule:\n(N'oubliez pas les variables u et v...)\n")
    temp = temp.split(',')
    return temp
    
def contraintes(X):
    nbrContrainte = int(input("Entrez le nombre de contrainte de votre problème:\n"))
    contrainteTab = []
    A = [[]for i in range(nbrContrainte)]
    B = []
    for i in range(nbrContrainte):
        print("\nContrainte numéro " + str(i) +":")
        for j in range(len(X)-nbrContrainte):
            temp = int(input("Entrez le coefficiant devant la variable " + X[j] + ": "))
            A[i].append(temp)
        temp = int(input("Entrez le membre droit de l'inéquation\n(Exemple: Si 3x-5y<=4, entrez 4): "))
        B.append(temp)
    v = np.ones(nbrContrainte)
    diag = np.diag(v)
    A = np.concatenate((A,diag),axis=1)
    return A,B
    
def fonctionAMaximiser(X,B):
    C = []
    for i in range(len(X)-len(B)):
        temp = int(input("Entrez le coefficiant devant la variable " + X[i] + " de la fonction à maximiser: "))
        C.append(temp)
    while len(C)!=len(X):
        C.append(0)
    return C
        

X = nbrDeVariable()
A,B = contraintes(X)
C = fonctionAMaximiser(X,B)
print(X)
print(A)
print(B)
print(C)