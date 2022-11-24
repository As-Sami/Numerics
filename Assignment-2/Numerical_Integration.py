def Trapezoidal(exp, a, b, n):
    
    def f(x):
        from math import log, sin, cos, tan, e, pi
        return eval(exp.replace('x', str(x)))
    
    h = (b - a) / n
    
    result = f(a) + f(b)
    for i in range(1, n):
        result += 2 * f(a + i*h)
        
    result *= (b-a) / (2*n)
    return result
    
def Simpson(exp, a, b, n):
    def f(x):
        from math import log, sin, cos, tan, e, pi
        return eval(exp.replace('x', str(x)))
    
    h = (b - a) / n
    
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4 * f(a + i*h)
    
    for i in range(2, n-1, 2):
        result += 2 * f(a + i*h)
        
    result *= (b-a) / (3 * n)
    return result

# print(Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 1))
# print(Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 2))
# print(Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 3))
# print(Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 4))
# print(Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 5))
# print(Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 6))
# print(Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 7))
# print(Trapezoidal('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 8))

# print('')

# print(Simpson('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 1))
# print(Simpson('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 2))
# print(Simpson('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 3))
# print(Simpson('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 4))
# print(Simpson('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 5))
# print(Simpson('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 6))
# print(Simpson('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 7))
# print(Simpson('2000 * log(140000/ (140000 - 2100*x)) - 9.8 * x', 8, 30, 8))

