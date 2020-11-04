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


def simplex(X, A, B, Z):
    print(A)
    #print(B)
    print(Z)
    minvaluecolunm = min(Z)
    minindexcolumn = np.where(Z == Z.min())[0][0]
    if minvaluecolunm >= 0:
        print("Solution optimal", Z)
    else:
        minindexrow = 0
        temp = []
        for index, value in enumerate(A[:, minindexcolumn]):
            if B[index] / value > 0:
                temp.append(B[index] / value)
        minindexrow = np.where(temp == min(temp))[0][0]
        if B[minindexrow] / A[minindexrow, minindexcolumn] <= 0:
            print("infinite solutions")
        else:
            AA = np.zeros(A.shape)
            BB = np.zeros(B.shape)
            linepivot = A[minindexrow, :] / A[minindexrow, minindexcolumn]
            valuepivot = B[minindexrow] / A[minindexrow, minindexcolumn]
            for index, value in enumerate(A):
                if index != minindexrow:
                    AA[index] = value - A[index, minindexcolumn] * linepivot
                    BB[index] = B[index] - A[index, minindexcolumn] * valuepivot
                elif index == minindexrow:
                    AA[index] = linepivot
                    BB[index] = valuepivot
            ZZ = Z - (Z[minindexcolumn]/A[minindexrow, minindexcolumn]) * A[minindexrow, :]
            simplex(X, AA, BB, ZZ)


if __name__ == '__main__':
    # X = nbrDeVariable()
    # A,B = contraintes(X)
    # C = fonctionAMaximiser(X,B)
    # print(X)
    # print(A)
    # print(B)
    # print(C)
    X = np.array(['x', 'y', 'u', 'v', 'w'])
    A = np.array([[2, 1, 1, 0, 0], [2, 3, 0, 1, 0], [3, 1, 0, 0, 1]])
    B = np.array([18, 42, 24])
    C = np.array([3, 2, 0, 0, 0])
    simplex(X, A, B, -C)
