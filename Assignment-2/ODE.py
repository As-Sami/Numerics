def Euler_Method(dexp, y_0, x_0, x_last, h):
    
    def f(x, y):
        from math import log, sin, cos, tan, e, pi
        return eval(dexp.replace('x', str(x)).replace('y', str(y)))
    
    
    
    while x_0 < x_last:
        y = y_0 + f(x_0, y_0) * h
        x_0 += h
        y_0 = y

    print(y_0)
    
    return y_0


def Heun(dexp, y_0, x_0, x_last, h):
    
    def f(x, y):
        from math import log, sin, cos, tan, e, pi
        return eval(dexp.replace('x', str(x)).replace('y', str(y)))
    
    step = (x_last - x_0) // h
    
    while x_0 < x_last:
        k1 = f(x_0, y_0)  
        k2 = f(x_0 + h , y_0 + k1*h )
                            
        y = y_0 + (k1/2 + k2/2)*h
        y_0 = y
        x_0 = x_0 + h    
    
    print(y_0)
    return y_0

def Midpoint(dexp, y_0, x_0, x_last, h):
    
    def f(x, y):
        from math import log, sin, cos, tan, e, pi
        return eval(dexp.replace('x', str(x)).replace('y', str(y)))
        
    while x_0 < x_last:
        k1 = f(x_0, y_0)  
        k2 = f(x_0 + h/2 , y_0 + k1*h/2 )
                            
        y = y_0 + k2*h
        y_0 = y
        x_0 = x_0 + h    
    
    print(y_0)
    return y_0
    
def Ralston(dexp, y_0, x_0, x_last, h):
    
    def f(x, y):
        from math import log, sin, cos, tan, e, pi
        return eval(dexp.replace('x', str(x)).replace('y', str(y)))
    
    while x_0 < x_last:
        k1 = f(x_0, y_0)  
        k2 = f(x_0 + h*3/4 , y_0 + k1*h*3/4 )
                            
        y = y_0 + (k1 / 3 + 2 * k2 / 3) * h
        y_0 = y
        x_0 = x_0 + h    
    
    print(y_0)
    return y_0


# Euler_Method('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 480)
# Heun('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 480)
# Midpoint('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 480)
# Ralston('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 480)

# print('')

# Euler_Method('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 240)
# Heun('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 240)
# Midpoint('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 240)
# Ralston('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 240)

# print('')

# Euler_Method('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 120)
# Heun('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 120)
# Midpoint('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 120)
# Ralston('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 120)

# print('')

# Euler_Method('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 60)
# Heun('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 60)
# Midpoint('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 60)
# Ralston('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 60)

# print('')

# Euler_Method('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 30)
# Heun('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 30)
# Midpoint('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 30)
# Ralston('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 30)