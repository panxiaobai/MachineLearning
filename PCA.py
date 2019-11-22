import numpy as np



def eig(x):
    pass


def SVD(A):
    AtA = np.dot(A.T, A)
    AAt = np.dot(A, A.T)

    AtAe, AtAv = np.linalg.eig(AtA)
    AAte, AAtv = np.linalg.eig(AAt)
    print(AAt)
    print(AAte)
    print(AAtv)
    dia=np.eye(A.shape[0],A.shape[1])*np.sqrt(AtAe)
    print(dia)
    return AAtv,dia,AtAv.T



A=np.mat([[0,1],[1,1],[1,0]])
print(A)

U,dia,V=np.linalg.svd(A)

print(U)
print(dia)
print(V)


