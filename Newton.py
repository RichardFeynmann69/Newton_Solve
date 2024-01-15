import numpy as np
import configparser

#Load from Config file (Use absolute path)
config = configparser.ConfigParser()
config.sections()
config.read('./config.ini')

#up_limit = float(config["EQ"]["up_limit"])
#low_limit = float(config["EQ"]["low_limit"])
#value_string= config["EQ"]["value"]
#value= eval(value_string)

#Create initial Matrix F values
x=float(config["EQ"]["x"])
y=float(config["EQ"]["y"])
h=e=0.000001
f = open("./output.txt", "w")

#Normal functions
def fn1(x,y):
    value_string= config["EQ"]["function1"]
    f1 = eval(value_string)
    return f1

def fn2(x,y):
    value_string= config["EQ"]["function2"]
    f2= eval(value_string)
    return f2

#Functions for derivative
#X functions
def fn_D1X(x,y,e):
    value_string= config["EQ"]["function1Dx"]
    f1 = eval(value_string)
    return f1

def fn_D2X(x,y,e):
    value_string= config["EQ"]["function2Dx"]
    f2= eval(value_string)
    return f2

#Y functions
def fn_D1Y(x,y,e):
    value_string= config["EQ"]["function1Dy"]
    f1 = eval(value_string)
    return f1

def fn_D2Y(x,y,e):
    value_string= config["EQ"]["function2Dy"]
    f2= eval(value_string)
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
    j11=D(fn2(xn,yn),fn_D2Y(xn,yn,e),h)
   

    F_matrix = np.array([[fn1(xn,yn)],[fn2(xn,yn)]])
    Jacobian_matrix = np.array([[j00,j01],[j10,j11]])
    P=np.linalg.inv(Jacobian_matrix)
    PF=np.dot(P,F_matrix)
    Xn=np.subtract(Xs,PF)
    counter += 1
    xa,ya = Xn.flatten()
    f.write(f"Rozwiazanie {counter}: x={round(xa,3)}, y={round(ya,3)} \n" )

f.close() 
print("Rozwiazanie w pliku")
  
    
