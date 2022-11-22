def Trapezoidal(exp, a, b, n):
    
    def f(x):
        from math import log, sin, cos, tan, e, pi
        return eval(exp.replace('x', str(x)))
    
    h = (b - a) / n
    
    result = f(a) + f(b)
    for i in range(1, n):
        result += 2 * f(a + i*h)
        
    result *= (b-a) / (2*n)
    print(result)

# Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 1)
# Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 2)
# Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 3)
# Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 4)
# Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 5)
# Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 6)
# Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 7)
# Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 8)

