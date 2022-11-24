def GEPP(A: list, b: list):
    '''Gaussian Elemination with Partial Pivoting'''
    n = len(A)   
    
    a = []
    
    for x in A:
        e = [];
        for y in x:
            e.append(y)
        a.append(e)
    
    for i in range(n):
        a[i].append(b[i])
        
    for k in range(n-1):
        pos = k
        val = a[k][k]
        
        for i in range(k+1, n):
            if val < a[i][k]:
                pos = i
                val = a[i][k]
        
        a[k], a[pos] = a[pos], a[k]
              
        temp = a[k].copy()
        val =  temp[k]
        for i in range(len(temp)):
            try:
                temp[i] /= val
            except:
                print('divison by zero')
                return None
        
        for i in range(k+1, n):
            temp2 = temp.copy()
            for j in range(len(temp2)):
                temp2[j] *= a[i][k]
            
            for j in range(len(a[i])):
                a[i][j] -= temp2[j]
    
        
    solution = [0] * n
    for i in range(n-1, -1, -1):
        j = i+1
        while j<n:
            a[i][n] -= a[i][j]*solution[j]
            j += 1
        
        solution[i] = a[i][n] / a[i][i]
        
    return solution

def find_points(x, y, n, target_x):
    
    points = [ [x[i],y[i]] for i in range(len(x)) ]
    points.sort()
    
    
    i = 0
    while i < len(x) and points[i][0] < target_x:
        i += 1
    
    if n==2:
        return [points[i][0], points[i-1][0]] , [points[i][1], points[i-1][1]]
    
    if n==3:
        return [points[i-1][0], points[i-2][0], points[i][0]] , [points[i-1][1], points[i-2][1], points[i][1]]
    
    if n==4:
        return [points[i-1][0], points[i-2][0], points[i][0], points[i+1][0]] , [points[i-1][1], points[i-2][1], points[i][1], points[i+1][1]]

def find_points(x, y, n, x1):
    diff = []
    for i in range(n):
        diff.append([abs(x[i]-x1),x[i],y[i]])

    diff.sort()
    xl = []
    yl = []
    for i in range(n+1):
        xl.append(diff[i][1])
        yl.append(diff[i][2])
    return xl,yl

def Linear_Interpolation(x, y, target_x):
    
    x, y = find_points(x, y, 2, target_x)
    
    x0, x1 = x
    y0, y1 = y
    
    # print(x, y)
    
    a1 = (y0 - y1) / (x0 - x1)
    a0 = y0 - a1*x0

    y_target = a0 + a1*target_x
    return y_target


def Quadratic_Interpolation( x, y, target_x):

    x, y = find_points(x, y, 3, target_x)
    
    a = []

    for i in range(3):
        a.append( [1, x[i], x[i]**2] )
        
    b = GEPP(a, y)
    
    target_y = b[0] + b[1] * target_x + b[2] * target_x**2
    return target_y
    


def Cubic_Interpolation( x, y, target_x):
    
    x, y = find_points(x, y, 4, target_x)
        
    a = []

    for i in range(4):
        a.append( [1, x[i], x[i]**2, x[i]**3] )
        
    b = GEPP(a, y)
    
    target_y = b[0] + b[1] * target_x + b[2] * target_x**2 + b[3] * target_x**3
    return target_y
    

def Linear_Lagrangian_Interpolation(x, y, target_x):
    
    x, y = find_points(x, y, 2, target_x)
    
    x0, x1 = x
    y0, y1 = y
    
    L0 = (target_x - x1) / (x0 - x1)
    L1 = (target_x - x0) / (x1 - x0)
    
    target_y = L0 * y0 + L1 * y1
    return target_y
    
    
def Quadratic_Lagrangian_Interpolation(x, y, target_x):
    x, y = find_points(x, y, 3, target_x)
    
    L = []
    
    for i in range(3):
        mul = 1
        for j in range(3):
            if i != j:
                mul *= (target_x - x[j]) / (x[i] - x[j])
        L.append(mul)
    
    target_y = 0
    for i in range(3):
        target_y += L[i] * y[i]
        
    return target_y
        

def Cubic_Lagrangian_Interpolation(x, y, target_x):
    
    x, y = find_points(x, y, 4, target_x)
    
    L = []
    
    for i in range(4):
        mul = 1
        for j in range(4):
            if i != j:
                mul *= (target_x - x[j]) / (x[i] - x[j])
        L.append(mul)
    
    target_y = 0
    for i in range(4):
        target_y += L[i] * y[i]
        
    return target_y
    

def Linear_Newton_DD(x, y, target_x):
    x, y = find_points(x, y, 2, target_x)
    
    x0, x1 = x
    y0, y1 = y
    
    b0 = y0
    b1 = (y1 - y0) / (x1 - x0)
    
    target_y = b0 + b1 * (target_x - x0)
    return target_y
    

def Quadratic_Newton_DD(x, y, target_x):
    x, y = find_points(x, y, 3, target_x)
    
    b0 = y[0]
    b1 = (y[1] - y[0]) / (x[1] - x[0])
    b2 = (( (y[2]-y[1]) / (x[2] - x[1]) ) - ( (y[1] - y[0]) / (x[1] - x[0]) )) / (x[2] - x[0])
    
    target_y = b0 + b1 * (target_x - x[0]) + b2 * (target_x - x[0]) * (target_x-x[1])
    return target_y
    

def Cubic_Newton_DD(x, y, target_x):
    x, y = find_points(x, y, 4, target_x)
    
    b0 = y[0]
    b1 = (y[1] - y[0]) / (x[1] - x[0])
    b2 = (( (y[2]-y[1]) / (x[2] - x[1]) ) - ( (y[1] - y[0]) / (x[1] - x[0]) )) / (x[2] - x[0])
    b3 = ( ( ( (y[3] - y[2]) / (x[3] - x[2]) - (y[2] - y[1]) / (x[2] - x[1]) ) / (x[3] - x[1]) ) - ( ( ( (y[2] - y[1])/(x[2] - x[1]) ) - ((y[1] - y[0]) / (x[1] - x[0])) ) / (x[2] - x[0]) ) ) / (x[3] - x[0])
    
    target_y = b0 + b1 * (target_x - x[0]) + b2 * (target_x - x[0]) * (target_x-x[1]) 
    target_y += b3 * (target_x - x[0]) * (target_x - x[1]) * (target_x - x[2])
    return target_y
    
        

x = [0, 10, 15, 20, 22.5, 30]
y = [0, 227.04, 362.78, 517.35, 602.97, 901.67 ]



print(Linear_Interpolation(x,y, 16))
print(Quadratic_Interpolation(x,y, 16))
print(Cubic_Interpolation(x,y, 16))

print(Linear_Lagrangian_Interpolation(x,y, 16))
print(Quadratic_Lagrangian_Interpolation(x,y, 16))
print(Cubic_Lagrangian_Interpolation(x,y, 16))

print(Linear_Newton_DD(x,y, 16))
print(Quadratic_Newton_DD(x,y, 16))
print(Cubic_Newton_DD(x,y, 16))