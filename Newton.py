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
    f2= y**3 - (x+e) +1
    return f2

#Y functions
def fn_D1Y(x,y,e):
    f1 = x**3 + (y+e) -1
    return f1

def fn_D2Y(x,y,e):
    f2= (y+e)**3 - x +1
    return f2

def D(fx,fxh,h):
    derivative = (fxh-fx)/h
    return derivative

xs=x+2*e
ys=y+2*e
Xs = np.array([[xs],[ys]])

xn=x
yn=y
Xn = np.array([[xn],[yn]])
counter = 0

while np.max(np.abs(Xn - Xs)) > e and counter<10:
    Xs=Xn
    xn, yn = Xn.flatten()
#Jacobian Values
    j00=D(fn1(xn,yn),fn_D1X(xn,yn,e),h)
    j10=D(fn2(xn,yn),fn_D2X(xn,yn,e),h)
    j01=D(fn1(xn,yn),fn_D1Y(xn,yn,e),h)
    j11=D(fn2(xn,y),fn_D2Y(xn,yn,e),h)
   

    F_matrix = np.array([[fn1(xn,yn)],[fn2(xn,yn)]])
    Jacobian_matrix = np.array([[j00,j01],[j10,j11]])
    P=np.linalg.inv(Jacobian_matrix)
    PF=np.dot(P,F_matrix)
    Xn=np.add(Xs,PF)
    counter += 1
    xa,ya = Xn.flatten()
    print(f"Rozwiązanie {counter}: x={xa}, y={ya}" )
    print("----------------------------------------")
    
