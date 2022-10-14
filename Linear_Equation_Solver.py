def NGE(A: list, b: list):
    '''Naive Gaussian Elemination'''
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
        
        temp = a[k].copy()
        val =  temp[k]
        for i in range(len(temp)):
            try:
                temp[i] /= val
            except:
                print('divison by zero')
                print("Naive Gaussian Elemination failed")
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

def LU(a: list):
    '''Converts a matrix to a upper and lower triangula matrix, A = L * U'''
    n = len(a)
    
    L = [[0 for i in range(n)] for j in range(n)]
    
    U = []
    
    for x in a:
        e = [];
        for y in x:
            e.append(y)
        U.append(e)
    
    for i in range(3):
        L[i][i] = 1      
    
    for k in range(n-1):
        pos = k
        val = U[k][k]
        
        temp = [1 for i in range(n)]
        for i in range(len(temp)):
            try:
                temp[i] /= val
            except:
                print('divison by zero')
                print("LU decomposition failed")
                return None, None
        
        for i in range(k+1, n):
            temp2 = temp.copy()
            
            for j in range(len(temp2)):
                temp2[j] *= U[i][k]
            
            L[i][k] = temp2[i]
            
            for j in range(len(a[i])):
                U[i][j] -= U[k][j]*temp2[j]
           
    return L, U

def LU_Decomposition(a, b):
    '''LU Decomposition'''
    n = len(a)
    L, U = LU(a)

    if L==None and U==None:
        return None

    Z = GEPP(L, b)
    
    for i in range(len(Z)):
        U[i].append(Z[i])
    
    solution = [0] * n
    for i in range(n-1, -1, -1):
        j = i+1
        while j<n:
            U[i][n] -= U[i][j]*solution[j]
            j += 1
        
        solution[i] = U[i][n] / U[i][i]
    
    return solution

def Inverse(a):
    '''Find the inverse of a matrix using LU decomposition method'''
    
    n = len(a)
    solution = []
    for i in range(n):
        solution.append([])
        
    for i in range(n):
        C = [0] * n
        C[i] = 1
        
        x = LU_Decomposition(a, C)
        if x == None:
            return None
        
        print(x)
        
        for j in range(n):
            solution[j].append(x[j])
  
    return solution