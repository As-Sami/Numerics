def Regression(x, y):
    
    n = len(x)
    
    xsum = sum(x)
    ysum = sum(y)
    
    xx = [i*i for i in x]
    xxsum = sum(xx)

    
    xysum = 0
    for i in range(n):
        xysum += x[i] * y[i]
    
    a1 = (n * xysum - xsum * ysum) / (n * xxsum - xsum**2)
    a0 = (xxsum * ysum - xsum*xysum) / (n * xxsum - xsum**2)
    
    return a0, a1
    
x = [0.698132, 0.959931, 1.134464, 1.570796, 1.919862]
y = [0.188224, 0.209138, 0.230052, 0.250965, 0.313707]

Regression(x, y)