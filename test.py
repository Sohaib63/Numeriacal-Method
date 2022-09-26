import BackwardDiffTable
import bisection
import DerNBackInt
import DerNForInt
import Euler
import ForwardDiffTable
import Guass_seidal
import jacobi
import NBackInterp
import newton_raphson
import NForInterp
import regular_falsi
import secant
import SimpleIterative
import Trapezoidal

print("Backward Difference Table")
print("Bisection")
print("Derivative Using Newton Backward Interpolation")
print("Derivative Using Newton Forward Interpolation")
print("Euler")
print("Forward Difference Table")
print("Guass_seidal")
print("Jacobi")
print("Newton Backward Interpolation")
print("Newton Raphson")
print("Newton Forward Interpolation")
print("Regular Falsi")
print("Secant")
print("Simple Iterative")
print("Trapezoidal")
flag=1
option=0
while(flag):
    option=int(input("Select Method: "))
    if (option<1 or option>15):
        flag=0
    if (option==1):
        BackwardDiffTable.P1()
    if (option==2):
        bisection.P2
    if (option==3):
        DerNBackInt.P3
    if (option==4):
        DerNForInt.P4
    if (option==5):
        Euler.P5
    if (option==6):
        ForwardDiffTable.P6
    if (option==7):
        Guass_seidal.P7
    if (option==8):
        jacobi.P8
    if (option==9):
        NBackInterp.P9
    if (option==10):
        newton_raphson.P10
    if (option==11):
        NForInterp.P11
    if (option==12):
        regular_falsi.P12
    if (option==13):
        secant.P13
    if (option==14):
        SimpleIterative.P14
    if (option==15):
        Trapezoidal.P15
    