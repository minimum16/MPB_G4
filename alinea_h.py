import pandas as pd
import numpy as np
import numdifftools as nd
import sympy as sym
from scipy.optimize import fsolve
from sympy import *


#sympy symbols
# X, S, A, P = symbols('X,S,A,P')

X, S, A, P, V, k1, k2, k3, k4, k11, Fin, Se = symbols('X,S,A,P,V,k1,k2,k3,k4,k11,Fin,Se')

#Reactions
u1 = 0.25 * (S / (0.3 + S))
u2 = 0.55 * (S / (0.3 + S))
u3 = 0.25 * (A / (0.4 + A))

# # Initial conditions
# X0= 7 #g/L
# S0= 12 #g/L
# A0= 0 #g/L
# P0= 0 #g/L
#V= 6 #L

# Parameters
# k1= 4.412
# k2= 22.22
# k3= 8.61
# k4= 9.846
# k5= 3.253
# k6= 12.29
# k7= 4.085
# k8= 3.345
# k9= 21.04
# k10= 7.65
# k11= 13.21
# V0= 6 #o volume inicial não se altera
# Se= 350 #concentração do substrato de entrada g/L
# Fin= 0.7 #L/h || caudal de entrada || 350 g/L glucose
# Fout= Fin #caudal de saida


difX= u1 * X + u2 * X + u3 * X - Fin/V * X
difS= - k1 * u1 * X - k2 * u2 * X + Fin/V * Se - Fin/V * S
difA= k3 * u2 * X - k4 * u3 * X - Fin/V * A
difP= k11 * u1 * X - Fin/V * P
difV= Fin - Fin
todas= [difX, difS, difA, difP]


def derX(t=False):
    dX = [sym.diff(difX, X), sym.diff(difX, S), sym.diff(difX, A), sym.diff(difX, P)]
    if t == True:
        print('Derivada X X:')
        print(sym.diff(difX, X))
        print()
        print('Derivada X S:')
        print(sym.diff(difX, S))
        print()
        print('Derivada X A:')
        print(sym.diff(difX, A))
        print()
        print('Derivada X P:')
        print(sym.diff(difX, P))
    return dX


def derS(t=False):
    dS = [sym.diff(difS, X), sym.diff(difS, S), sym.diff(difS, A), sym.diff(difS, P)]
    if t == True:
        print('Derivada S X:')
        print(sym.diff(difS, X))
        print()
        print('Derivada S S:')
        print(sym.diff(difS, S))
        print()
        print('Derivada S A:')
        print(sym.diff(difS, A))
        print()
        print('Derivada S P:')
        print(sym.diff(difS, P))
    return dS


def derA(t=False):
    dA = [sym.diff(difA, X), sym.diff(difA, S), sym.diff(difA, A), sym.diff(difA, P)]
    if t == True:
        print('Derivada A X:')
        print(sym.diff(difA, X))
        print()
        print('Derivada A S:')
        print(sym.diff(difA, S))
        print()
        print('Derivada A A:')
        print(sym.diff(difA, A))
        print()
        print('Derivada A P:')
        print(sym.diff(difA, P))
    return dA


def derP(t=False):
    dP = [sym.diff(difP, X), sym.diff(difP, S), sym.diff(difP, A), sym.diff(difP, P)]
    if t == True:
        print('Derivada P X:')
        print(sym.diff(difP, X))
        print()
        print('Derivada P S:')
        print(sym.diff(difP, S))
        print()
        print('Derivada P A:')
        print(sym.diff(difP, A))
        print()
        print('Derivada P P:')
        print(sym.diff(difP, P))
    return dP

derX()
#print('='*66)
derS()
#print('='*66)
derA()
#print('='*66)
derP()


def fun(x):
    X, S, A, P = x
    # Reactions
    u1 = 0.25 * (S / (0.3 + S))
    u2 = 0.55 * (S / (0.3 + S))
    u3 = 0.25 * (A / (0.4 + A))

    # Initial conditions
    S0 = 12 # g/L

    # Parameters
    k1 = 4.412
    k2 = 22.22
    k3 = 8.61
    k4 = 9.846
    k11 = 13.21
    Fin = 0.7
    Se = 350
    V = 6

    return [(u1 * X + u2 * X + u3 * X - Fin/V * X),
            (- k1 * u1 * X - k2 * u2 * X + Fin/V * Se - Fin/V * S),
            (k3 * u2 * X - k4 * u3 * X - Fin/V * A),
            (k11 * u1 * X - Fin/V * P)]


root = fsolve(fun, [0, 0, 0, 0])
print(root)
print(np.isclose(fun(root), [0.0, 0.0, 0.0, 0.0]))
print()
root1 = fsolve(fun, [7, 0, 0, 0])
print(root1)
print(np.isclose(fun(root1), [0.0, 0.0, 0.0, 0.0]))
print()


def Jacobian(v_str, f_list):
    global J
    vars = sym.symbols(v_str)
    f = sym.sympify(f_list)
    J = sym.zeros(len(f),len(vars))
    for i, fi in enumerate(f):
        for j, s in enumerate(vars):
            J[i, j] = sym.diff(fi, s)
    J = np.array(J).tolist()
    print(J)
    return J
Jacobian('X G A P', ['u1*X + u2*X + u3*X - Fin/V*X',' - k1*u1*X - k2*u2*X + Fin/V*Se - G*Fin/V', 'k3*u2* X - k4*u3*X - Fin/V*A', 'k11*u1*X - Fin/V*P']) #tem de ser G em vez de S para o substrato

#jacobiano
#[[-Fin/V + u1 + u2 + u3, 0, 0, 0], [-k1*u1 - k2*u2, -Fin/V, 0, 0], [k3*u2 - k4*u3, 0, -Fin/V, 0], [k11*u1, 0, 0, -Fin/V]]


# k1 = 4.412
# k2 = 22.22
# k3 = 8.61
# k4 = 9.846
# k11 = 13.21
# Fin = 0.7
# V = 6


#ponto 1
#X1, G1, A1, P1 = 0, 350, 0, 0
# u1 = 0.24979
# u2 = 0.54953
# u3 = 0

JJ = [[0.68265, 0, 0, 0], [-13.31263, -0.11667, 0, 0], [4.73145, 0, -0.11667, 0], [3.29973, 0, 0, -0.11667]]
JJJ = np.array(JJ)
jjjj = np.linalg.det(JJJ)
print('O determinante do ponto 1 é {}'.format(jjjj))
jjjjj = np.trace(JJJ)
print('O traço do ponto 1 é {}'.format(jjjjj))

#ponto instavel sela


#ponto 2
#X2, S2, A2, P2 = 33.6371514, 0.0300697191, 0.0849325999, 86.7438978
# u1 = 0.02278
# u2 = 0.05011
# u3 = 0.04379

LL = [[-0.04334, 0, 0, 0], [-1.21395, -0.11667, 0, 0], [0.00029, 0, -0.11667, 0], [0.30092, 0, 0, -0.11667]]
LLL = np.array(LL)
llll = np.linalg.det(LLL)
print('O determinante do ponto 2 é {}'.format(llll))
lllll = np.trace(LLL)
print('O traço do ponto 2 é {}'.format(lllll))


#ponto estavel