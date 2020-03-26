#Name: Hayden Tam
# Instructor: S. Einakian
# Class: CPE 101-05
import copy
#Purpose: add list of same polynomials with one another
#Signature: list,list-> list
def poly_add2(x,y):
    
    z1=x[0]+y[0]
    z2=x[1]+y[1]
    z3=x[2]+y[2]
    z=[z1,z2,z3]
    return z

#Purpose: Multiply through FOIL of two lists of degree two
#signature: list, list-> list
def poly_mult2(x,y):
    z=[]
    z1=x[0]*y[0]
    z2=x[0]*y[1]+x[1]*y[0]
    
    z3=x[0]*y[2]+x[2]*y[0]+y[1]*x[1]
    z4=x[2]*y[1]+x[1]*y[2]
    z5=y[2]*x[2]
    z.append(z1)
    z.append(z2)
    z.append(z3)
    z.append(z4)
    z.append(z5)
    return z



