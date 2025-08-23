from sympy import *
import display from 
init_printing()

A = Matrix([[3,1,1],[1,-2,+1],[2,1,1],[1,3,1]])
y = Matrix([10,5,-6,6])

AtA = A.T*A
Aty = A.T*y


display(Matrix.hstack(AtA, Aty).rref()[0][:,-1])