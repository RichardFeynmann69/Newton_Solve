import numpy as np
import configparser

#Load from Config file (Use absolute path)
config = configparser.ConfigParser()
config.sections()
config.read('./config.ini')

#up_limit = float(config["EQ"]["up_limit"])
#low_limit = float(config["EQ"]["low_limit"])

#Create initial Matrix F values
x=0.9
y=0.9
h=e=0.000001

#Normal functions
def fn1(x,y):
    f1 = x**3 + y -1
    return f1

def fn2(x,y):
    f2= y**3 - x +1
    return f2

#Functions for derivative
#X functions
def fn_D1X(x,y,e):
    f1 = (x+e)**3 + y -1
    return f1

def fn_D2X(x,y,e):
    f2= y**3 - (x+e) -1
    return f2

#Y functions
def fn_D1Y(x,y,e):
    f1 = x**3 + (y+e) -1
    return f1

def fn_D2Y(x,y,e):
    f2= (y+e)**3 - x -1
    return f2

def D(fx,fxh,h):
    derivative = (fx-fxh)/h
    return derivative

xs=x-2*e
ys=y-2*e
Xs = np.array([[xs],[ys]])

xn=x
yn=y
Xn = np.array([[xn],[yn]])
E= np.array([[e],[e]])

for i in range(10):
#Jacobian Values
    j00=D(fn1(x,y),fn_D1X(x,y,e),h)
    j01=D(fn2(x,y),fn_D2X(x,y,e),h)
    j10=D(fn1(x,y),fn_D1Y(x,y,e),h)
    j11=D(fn2(x,y),fn_D2Y(x,y,e),h)

    F_matrix = np.array([[fn1(x,y)],[fn2(x,y)]])
    Jacobian_matrix = np.array([[j00,j01],[j10,j11]])
    P=np.linalg.inv(Jacobian_matrix)

    Xn=np.subtract(Xs,np.dot(P,F_matrix))
    Xs=Xn
    if i==9:
        print(Xn)
