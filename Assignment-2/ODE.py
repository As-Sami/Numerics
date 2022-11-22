def Euler_Method(dexp, y_0, x_0, x_last, h):
    
    def f(x, y):
        return eval(dexp.replace('x', str(x)).replace('y', str(y)))
    
    step = (x_last - x_0) // h
    y_prev = y_0
    x_prev = x_0
    
    for i in range(step):
        y = y_prev + f(x_prev, y_prev) * h
        x_prev += h
        y_prev = y

    print(y_prev)


def Heun(dexp, y_0, x_0, x_last, h):
    
    def f(x, y):
        return eval(dexp.replace('x', str(x)).replace('y', str(y)))
    
    step = (x_last - x_0) // h
    y_prev = y_0
    x_prev = x_0
    
    for i in range(step):
        k1 = f(x_prev, y_prev)  
        k2 = f(x_prev + h , y_prev + k1*h )
                            
        y = y_prev + (k1/2 + k2/2)*h
        y_prev = y
        x_prev = x_prev + h    
    print(y_prev)

def Midpoint(dexp, y_0, x_0, x_last, h):
    
    def f(x, y):
        return eval(dexp.replace('x', str(x)).replace('y', str(y)))
    
    step = (x_last - x_0) // h
    y_prev = y_0
    x_prev = x_0
    
    for i in range(step):
        k1 = f(x_prev, y_prev)  
        k2 = f(x_prev + h/2 , y_prev + k1*h/2 )
                            
        y = y_prev + k2*h
        y_prev = y
        x_prev = x_prev + h    
    print(y_prev)
    
def Ralston(dexp, y_0, x_0, x_last, h):
    
    def f(x, y):
        return eval(dexp.replace('x', str(x)).replace('y', str(y)))
    
    step = (x_last - x_0) // h
    y_prev = y_0
    x_prev = x_0
    
    for i in range(step):
        k1 = f(x_prev, y_prev)  
        k2 = f(x_prev + h*3/4 , y_prev + k1*h*3/4 )
                            
        y = y_prev + (k1 / 3 + 2 * k2 / 3) * h
        y_prev = y
        x_prev = x_prev + h    
    print(y_prev)


Euler_Method('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 240)
Heun('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 240)
Midpoint('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 240)
Ralston('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 240)

print('')

Euler_Method('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 120)
Heun('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 120)
Midpoint('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 120)
Ralston('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 120)

print('')

Euler_Method('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 60)
Heun('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 60)
Midpoint('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 60)
Ralston('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 60)

print('')

Euler_Method('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 30)
Heun('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 30)
Midpoint('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 30)
Ralston('-2.2067 * 10**(-12) * (y**4 - 81 * 10 ** 8) ', 1200, 0, 480, 30)