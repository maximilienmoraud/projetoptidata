# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np


def nbrDeVariable():
    temp = input(
        "Entrez les noms de vos variables en les séparants par une virgule:\n(N'oubliez pas les variables u et v...)\n")
    temp = temp.split(',')
    return temp


def contraintes(X):
    nbrContrainte = int(input("Entrez le nombre de contrainte de votre problème:\n"))
    contrainteTab = []
    A = [[] for i in range(nbrContrainte)]
    B = []
    for i in range(nbrContrainte):
        print("\nContrainte numéro " + str(i) + ":")
        for j in range(len(X) - nbrContrainte):
            temp = int(input("Entrez le coefficiant devant la variable " + X[j] + ": "))
            A[i].append(temp)
        temp = int(input("Entrez le membre droit de l'inéquation\n(Exemple: Si 3x-5y<=4, entrez 4): "))
        B.append(temp)
    v = np.ones(nbrContrainte)
    diag = np.diag(v)
    A = np.concatenate((A, diag), axis=1)
    return A, B


def fonctionAMaximiser(X, B):
    C = []
    for i in range(len(X) - len(B)):
        temp = int(input("Entrez le coefficiant devant la variable " + X[i] + " de la fonction à maximiser: "))
        C.append(temp)
    while len(C) != len(X):
        C.append(0)
    return C


def simplex(X, A, B, C):
    Z = C
    minindexcolumn = 0
    minindexrow = -1
    for index, value in enumerate(Z):
        if value < 0 and value < Z[minindexcolumn]:
            minindexcolumn = index
    if Z[minindexcolumn] == 0:
        print("Solution optimal", Z)
    else:
        for index, value in enumerate(A[:, minindexcolumn]):
            if value != 0 and value < A[minindexrow, minindexcolumn]:
                minindexrow = index
        if A[minindexrow, minindexcolumn] == -1:
            print("infinite solutions")
        else:
            E = np.array()
            print(E)
            for index, value in enumerate(A):
                if A[index, minindexcolumn] > 0:
                    line = value - A[index, minindexcolumn] * (A[minindexrow, :] * (1 / A[index, minindexcolumn]))
                    E = np.concatenate((E, line), axis=0)
            print(E)


if __name__ == '__main__':
    # X = nbrDeVariable()
    # A,B = contraintes(X)
    # C = fonctionAMaximiser(X,B)
    # print(X)
    # print(A)
    # print(B)
    # print(C)
    X = np.array(['x', 'y', 'u', 'v', 'w'])
    A = np.array([[1, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1]])
    B = np.array([400, 300, 200])
    C = np.array([6, 3, 0, 0, 0])
    simplex(X, A, B, -C)
