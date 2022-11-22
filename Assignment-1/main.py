import Root_Finder
import Linear_Equation_Solver

print('''
Welcome.......
Which type of problem do you want to solve???
1. Root finding
2. Solving system of linear equation
''')

def input_general():
    exp = input('Enter the function : ')
    tolerance = float(input('Enter tolerance value : '))
    iteration = int(input('Enter iteration number: '))
    
    exp = exp.replace('^', '**')
    
    return exp, tolerance, iteration

def input_1(type):
    exp, tolerance, iteration = input_general()
    
    while True:
        first_guess = float(input('Enter your first guess: '))
        second_guess = float(input('Enter your second guess: '))
        
        if type == 1:
            result = Root_Finder.Bisection(exp, tolerance, iteration, first_guess, second_guess)
        elif type == 2:
            result = Root_Finder.FalsePosition(exp, tolerance, iteration, first_guess, second_guess)
        elif type == 4:
            result = Root_Finder.Secant(exp, tolerance, iteration, first_guess, second_guess)
            
        if result[0]==None and result[1] == None:
            continue
        else:
            Root_Finder.Show_A(result)
            break

def input_2():
    exp, tolerance, iteration = input_general()
    first_guess = float('Enter your initial guess: ')
    
    result = Root_Finder.NewtonRaphson(exp, tolerance, iteration, first_guess)
    Root_Finder.Show_A(result)
    

def f1():
    print('''Enter the method to solve the equation
    1. Bisection Method
    2. False Position Method
    3. Newton Raphson Method
    4. Secant Method
    ''')
    
    while True:
        op = input('Enter the your choice(1/2/3/4 or type q to exit): ')
        if op == 'q':
            break
        elif op=='1':
            input_1(1)
            break
        elif op=='2':
            input_1(2)
            break
        elif op=='3':
            input_2()
            break
        elif op=='4':
            input_1(4)
            break

def input_matrix():
    n,m = map(int, input("Enter the size of matrix(n X m): ").split())
    print('Enter all element of each row in one line')
    a = []
    for i in range(n):
        a.append( map(int, input().split()) )
        
    return a

def print_matrix(name, a):
    print(a)
    for i in a:
        for j in i:
            print(format(j, f'.3f'), end=' ')
        print('')
    print('')

def print_solution(a, sol):
    print(a)
    for i in range(len(sol)):
        print(f'x({i+1}) = {sol[i]}')

def f2():
    print('''Enter the method to solve the equation
    1. Solve System of Linear Equation with Naive Gaussian Elemination
    2. Solve System of Linear Equation with Gaussian Elemination with Partial Pivoting
    3. Make a matrix A to L , U lower and upper triangular matrix
    4. Solve System of Linear Equation with LU decomposition
    5. Inverse a matrix
    ''')

    while True:
        op = input('Enter the your choice(1/2/3/4/5 or type q to exit): ')
        if op == 'q':
            break
        elif op=='1':
            a = input_matrix()
            print("enter C matrix in row matrix form")
            b = input_matrix()
            result = Linear_Equation_Solver.NGE(a,b)
            if result:
                print_solution('Solution by Naive Gaussian Elemination: ',result)
            break
            
        elif op=='2':
            a = input_matrix()
            print("enter C matrix in row matrix form")
            b = input_matrix()
            result = Linear_Equation_Solver.GEPP(a,b)
            if result:
                print_solution('Solution by Gaussian Elemination with Partial Pivoting: ',result)
            break
        
        elif op=='3':
            a = input_matrix()
            L, U = Linear_Equation_Solver.LU(a)
            if L == None and U == None:
                pass
            else:
                print_matrix("Lower tringular matrix : ", L)
                print_matrix("Upper tringular matrix : ", U)
            break
            
        elif op=='4':
            a = input_matrix()
            print("enter C matrix in row matrix form")
            b = input_matrix()
            result = Linear_Equation_Solver.LU_Decomposition(a,b)
            if result:
                print_solution('Solution by Gaussian Elemination with Partial Pivoting: ',result)
            break
        
        elif op == '5':
            a = input_matrix()
            inv = Linear_Equation_Solver.Inverse(a)
            
            if inv:
                print_matrix("inverse matrix : ", inv)
                
            break

while True:
    op = input('Enter the your choice(1/2 or type q to exit): ')
    if op == 'q':
        break
    elif op == '1':
        f1()
        break
    elif op == '2':
        f2()
        break
        