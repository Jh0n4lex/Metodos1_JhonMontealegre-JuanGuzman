import sympy as sym



x = sym.Symbol("x")

h = sym.Symbol("h")

X = [-2*h,-1*h,0*h,1*h,2*h]

def Lagrange(x,xi,j):
    
    prod = 1
    n = len(xi)
    
    for i in range(n):
        if i != j:
            prod *= (x - xi[i])/(xi[j]-xi[i])
            
    return prod


def GetCoefficients(x,X,p):
    Coefficients = []
    for i in range (len(X)):
        Li = Lagrange(x,X,i)
        dLi = sym.diff(Li,x)
        C = dLi.subs(x,X[p])
        Coefficients.append(C)
    return Coefficients

print(GetCoefficients(x,X,2))

"""
Primero, hay que tener en cuenta que la discretización
está definida por 5 puntos, por lo que el polinomio
interpolador de Lagrange será de grado 4. Además, el error
está asociado al grado de este polinomio interpador.
El error esta en h**4
"""


    
