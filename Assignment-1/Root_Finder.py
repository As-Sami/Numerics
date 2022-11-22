from sympy import diff, symbols
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

def Draw_Graph(exp, start, end):
    
    def f(x):
        return eval(exp.replace('x', str(x)))
    
    xx = []
    yy = []
    
    while start < end:
        xx.append(start)
        yy.append(f(start))
        start += 0.01
        
    plt.axhline(y=0.0, color='r', linestyle='-')
    plt.axvline(x=0.0, color='r')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    
    plt.plot(np.array(xx), np.array(yy))
    plt.show()
    

def Bisection(exp, tolerance, iteration, first_guess, second_guess):
    
    def f(x):
        return eval(exp.replace('x', str(x)))
    
    u = first_guess
    l = second_guess

    if f(u) * f(l) > 0:
        print('The initial guesses are the same sign... Please guess again')
        return None, None

    prev = None
    root = None
    table = [('Iteration', 'x(l)', 'x(u)', 'x(m)', 'error', 'f(x(m))')]

    for it in range(1, iteration):
        
        m = (u+l) / 2
        val_u = round(f(u), 6)
        val_m = round(f(m), 6)
        val_l = round(f(l), 6)
        
        err = None if prev is None else abs(abs(prev - m)/m) * 100

        table.append((it+1, l, u, m, err, val_m))
        prev = m
        
        if err and err < tolerance:
            root = m
            break
        
        if val_l * val_m < 0:
            u = m
        elif val_l * val_m > 0:
            l = m
        else:
            root = m
            break
        
    return root, table
    
def FalsePosition(exp, tolerance, iteration, first_guess, second_guess):
    
    def f(x):
        return eval(exp.replace('x', str(x)))
    
    u = first_guess
    l = second_guess
    
    if f(u) * f(l) > 0:
        print('The initial guesses are the same sign... Please guess again')
        return None, None
    
    prev = None
    root = None
    table = [('Iteration', 'x(l)', 'x(u)', 'x(m)', 'error', 'f(x(m))')]

    for it in range(1, iteration):
        
        val_u = f(u)
        val_l = f(l)
        
        m = (u * val_l - l * val_u) / (val_l - val_u)
        val_m = f(m)
        
        err = None if prev is None else abs(abs(prev - m)/m) * 100
                    
        table.append((it+1, l, u, m, err, val_m))
        
        if err and err < tolerance:
            root = m
            break
        
        if val_l * val_m < 0:
            u = m
        elif val_l * val_m > 0:
            l = m
        else:
            root = m
            break
        
        prev = m
        
    return root, table

def NewtonRaphson(exp, tolerance, iteration, initial_guess):

    def f(x):
        return eval(exp.replace('x', str(x)))
    
    d_exp = str(diff(exp, symbols('x')))
    
    def df(x):
        return eval(d_exp.replace('x', str(x)))

    x = initial_guess
    root = None
    table = [('Iteration', 'x(i)', 'x(i+1)', 'error')]
    
    for it in range(1, iteration):
        y = x - f(x)/df(x)
        
        err = abs((y - x)/y) * 100
        
        table.append((it, x, y, err))
        x = y
        it += 1
        
        if err > tolerance:
            continue
        else:
            root = x
            break
    
    return root, table
    
def Secant(exp, tolerance, itetarion, first_guess, second_guess):

    def f(x):
        return eval(exp.replace('x', str(x)))
    
    x = first_guess
    y = second_guess
    table = [('Iteration', 'x(i-1)', 'x(i)', 'x(i+1)', 'error')]
    root = None
    
    for it in range(1, itetarion+1):
        z = y - (f(y) * (y-x)) / (f(y) - f(x))
        
        err = abs((z - y)/z) * 100
        
        table.append((it, x, y, z, err))
        x = y
        y = z
        
        if err > tolerance:
            continue
        else:
            root = x
            break
    
    return root, table
    
def Show_A(info):
    root, table = info
    if root == None:
        print('Could not find the root with given tolerace')
    else:
        print('Root =', root)
    if table:
        print(tabulate(table[1:], headers=table[0]))
