#2変数のニュートン
import numpy as np
import math

def f(x,y):
    return math.sin(x) + y

def g(x,y):
    return x - math.cos(y)

X1=0
Y1=0

A2=np.array([[X1], [Y1]]) - (1 / ((math.cos(X1) * math.sin(Y1) )- 1)) * np.array([[math.sin(Y1), -1], [-1, math.cos(X1)]]) @ np.array([[f(X1,Y1)], [g(X1,Y1)]])

X2=A2[0,0]
Y2=A2[1,0]

A3=np.array([[X2], [Y2]]) - (1 / ((math.cos(X2) * math.sin(Y2) )- 1)) * np.array([[math.sin(Y2), -1], [-1, math.cos(X2)]]) @ np.array([[f(X2,Y2)], [g(X2,Y2)]])

X3=A3[0,0]
Y3=A3[1,0]


print(f"X1={X1} , Y1={Y1} , f(X1,Y1)={f(X1,Y1)} , g(X1,Y1)={g(X1,Y1)} , A2={A2} , X2={X2} , Y2={Y2} , A3={A3} , X3={X3} , Y3={Y3} ")
