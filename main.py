import numpy as np
import math


def nbrDeVariable():
    temp = input(
        "Entrez les noms de vos variables en les séparants par une virgule:\n(N'oubliez pas les contraites)\n")
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
            temp = float(input("Entrez le coefficiant devant la variable " + X[j] + ": "))
            A[i].append(temp)
        temp = float(input("Entrez le membre droit de l'inéquation\n(Exemple: Si 3x-5y<=4, entrez 4): "))
        B.append(temp)
    v = np.ones(nbrContrainte)
    diag = np.diag(v)
    A = np.concatenate((A, diag), axis=1)
    return A, B


def fonctionAMaximiser(X, B):
    C = []
    for i in range(len(X) - len(B)):
        temp = float(input("Entrez le coefficiant devant la variable " + X[i] + " de la fonction à maximiser: "))
        C.append(temp)
    while len(C) != len(X):
        C.append(0)
    return C


def simplex(X, A, B, Z, Base):
    minvaluecolunm = min(Z)
    minindexcolumn = np.where(Z == Z.min())[0][0]
    if minvaluecolunm >= 0:
        print("optimal solutions", B, Base)
    else:
        temp = []
        for index, value in enumerate(A[:, minindexcolumn]):
            if value != 0 and B[index] / value > 0:
                temp.append(B[index] / value)
            else:
                temp.append(math.inf)
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
            ZZ = Z - (Z[minindexcolumn] / A[minindexrow, minindexcolumn]) * A[minindexrow, :]
            Base[minindexrow] = np.copy(X[minindexcolumn])
            simplex(X, AA, BB, ZZ, Base)


if __name__ == '__main__':
    # X = nbrDeVariable()
    # A, B = contraintes(X)
    # C = fonctionAMaximiser(X, B)
    X = np.array(['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7'])
    A = np.array([[10, 15, 11, 12, 0, 8, 1, 0, 0, 0, 0, 0, 0], [12, 12, 12, 0, 12, 15, 0, 1, 0, 0, 0, 0, 0],
                  [0, 12, 13, 16, 0, 4.57, 0, 0, 1, 0, 0, 0, 0], [5, 6, 0, 0, 7.5, 6, 0, 0, 0, 1, 0, 0, 0],
                  [2, 1, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0], [10, 0, 10, 12, 8, 10, 0, 0, 0, 0, 0, 1, 0],
                  [0, 0, 12, 12, 14, 16, 0, 0, 0, 0, 0, 0, 1]])
    B = np.array([900, 1000, 700, 500, 150, 800, 800])
    C = np.array([2.1, 2.2, 1.8, 1.2, 1.6, 2.2, 0, 0, 0, 0, 0, 0, 0])
    defaultbase = np.copy(X[len(A[:, 1]) - 1:])

    simplex(X, A, B, -C, defaultbase)
