import customtkinter as ctk
import tkinter
import Interpolation

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('800x600')
        self.method = ''
        
        self.interpolation_result = ResultPage(self)
        self.result_integration = ResultPage_Integration(self)
        self.integration = IntegrationPage(self)
        self.home = FirstPage(self)
        
        self.interpolation = SecondPage(self)
    
    def to_interpolation_result(self, x, y, n, target):
        self.interpolation_result.store(x, y, n, target)
        self.interpolation_result.compute()
        self.interpolation_result.tkraise()
        
    def to_interpolation(self):
        self.interpolation.tkraise()
        
    def to_regression(self):
        self.integration.tkraise()
    
    def to_home(self):
        self.home.tkraise()
        
    # def to_integration_result(self, f, a, b, n):
    #     self.result_integration.store(f, a, b, n)
    #     self.result_integration.compute()
    #     self.result_integration.tkraise()
        
        
class FirstPage(ctk.CTkFrame):
    
    def __init__(self, parent):        
        super().__init__(master = parent, width=600, height=400, corner_radius=10)
        self.parent = parent
        self.place(x=100, y=100)
        
        self.label = ctk.CTkLabel(master = self, text='Choose your method', height=40, 
            width=300, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label.place(x=150, y=30)
        
                
        self.ODE = Button(self, "Interpolation", lambda : parent.to_interpolation(), 150, 140)
        self.integration = Button(self, "Linear Regression", lambda : parent.to_regression(), 150, 210)     
        
        
class Button(ctk.CTkButton):
    def __init__(self, parent, name, command, x, y):
        ctk.CTkButton.__init__(self, master = parent, text=name , height=40, corner_radius=20, width=300, 
            bg_color='#2a2d2e', text_font=("Cascadia Code ExtraLight", 13), command = command)
        self.place(x=x, y=y)

class CustomLabel(ctk.CTkLabel):
    def __init__(self, parent, text):
        ctk.CTkLabel.__init__(self, master = parent, text=text, height=40, width=100, corner_radius=10, text_font=("Cascadia Code", 12), bg_color='#123456')
  
class IntegrationPage(ctk.CTkFrame):
    
    def __init__(self, parent):        
        super().__init__(master = parent, width=600, height=400, corner_radius=10)
        self.parent = parent
        self.place(x=100, y=100)
        
        self.f = ctk.CTkEntry(master=self, placeholder_text="Enter the function here", width=350, height=40, 
            border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.f.place(x=100, y=70)  
        
        
        self.label1 = ctk.CTkLabel(master = self, text='Lower limit:', height=40, width=100, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label1.place(x=110, y=140)
        
        self.a = ctk.CTkEntry(master=self, placeholder_text="", width=150, height=40, border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.a.place(x=300, y=140)  
        
        self.label2 = ctk.CTkLabel(master = self, text='Upepr Limit:', height=40, width=100, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label2.place(x=110, y=200)
        
        self.b = ctk.CTkEntry(master=self, placeholder_text="", width=150, height=40, border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.b.place(x=300, y=200)  
        
        self.label4 = ctk.CTkLabel(master = self, text='Segment size: ', height=40, width=100, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label4.place(x=100, y=260)
        
        self.n = ctk.CTkEntry(master=self, placeholder_text="1,2,3,5,10", width=200, height=40, border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.n.place(x=300, y=260)  
        
        
        self.solve = ctk.CTkButton(master = self, text='Solve', height=50, corner_radius=25, width=200,
            bg_color='#2a2d2e',text_font=("Cascadia Code ExtraLight", 13), command=self.compute)
        self.solve.place(x=200, y=330)
        
        self.back = ctk.CTkButton(master = self, text='<-', height=30, corner_radius=15, width=30,
            bg_color='#2a2d2e',text_font=("Cascadia Code ExtraLight", 10), command=lambda : parent.to_home())
        self.back.place(x=10, y=10)
        
    def compute(self):
        f = self.f.get()
        a = self.a.get()
        b = self.b.get()
        n = self.n.get()
        
        # try:
        a = int(a)
        b = int(b)
        
        n = list(map(int, n.split(',')))
        from math import log, sin, cos, tan, e, pi
        eval(f.replace('x', str(a)))
        self.parent.to_integration_result(f, a, b, n)

        # except:
        #     print('error')
  
  
    
class SecondPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, width=600, height=400, corner_radius=10)
        self.parent = parent
        self.place(x=100, y=100)
                
        
        self.label1 = ctk.CTkLabel(master = self, text='Value of xi:', height=40, width=100, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label1.place(x=30, y=140)
        
        self.x = ctk.CTkEntry(master=self, placeholder_text="", width=400, height=40, border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.x.place(x=200, y=140)  
        
        self.label2 = ctk.CTkLabel(master = self, text='Value of yi:', height=40, width=100, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label2.place(x=30, y=200)
        
        self.y = ctk.CTkEntry(master=self, placeholder_text="", width=400, height=40, border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.y.place(x=200, y=200)  
        
        self.label3 = ctk.CTkLabel(master = self, text='Number of points:', height=40, width=100, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label3.place(x=30, y=80)
        
        self.n = ctk.CTkEntry(master=self, placeholder_text="", width=130, height=40, border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.n.place(x=250, y=80)
        
        self.label4 = ctk.CTkLabel(master = self, text='Target x:', height=40, width=100, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label4.place(x=30, y=260)
        
        self.target = ctk.CTkEntry(master=self, placeholder_text="the value of x to be calculated", width=300, height=40, border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.target.place(x=160, y=260)  
        
        
        self.solve = ctk.CTkButton(master = self, text='Solve', height=50, corner_radius=25, width=200,
            bg_color='#2a2d2e',text_font=("Cascadia Code ExtraLight", 13), command=self.compute)
        self.solve.place(x=200, y=330)
        
        self.back = ctk.CTkButton(master = self, text='<-', height=30, corner_radius=15, width=30,
            bg_color='#2a2d2e',text_font=("Cascadia Code ExtraLight", 10), command=lambda : parent.to_home())
        self.back.place(x=10, y=10)

    def compute(self):
        x = self.x.get()
        y = self.y.get()
        n = self.n.get()
        target = self.target.get()
        
        # try:
        x = list(map(float, x.split(',')))
        y = list(map(float, y.split(',')))
        n = int(n)
        target = float(n)
        self.parent.to_interpolation_result(x, y, n, target)
 
        # except:
        #     print('error')
            
class ResultPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, width=600, height=400, corner_radius=10)
        self.parent = parent
        self.place(x=100, y=100)
        
        self.label0 = CustomLabel(self, 'Method')
        self.label1 = CustomLabel(self, 'Linear')
        self.label2 = CustomLabel(self, 'Quadratic')
        self.label3 = CustomLabel(self, 'Cubic')
        
        self.label0.place(x=30, y=50)
        self.label1.place(x=150, y=50)
        self.label2.place(x=260, y=50)
        self.label3.place(x=370, y=50)

        self.results = []
        
        
    def store(self, x, y, n, target):
        self.x = x
        self.y = y
        self.n = n
        self.target = target
    
    def compute(self):
        
        print(self.target, self.n)
        print(self.x)
        print(self.y)
        
        l0 = CustomLabel(self, 'Linear')
        l1 = CustomLabel(self, 'Quadratic')
        l2 = CustomLabel(self, 'Cubic')
        
        l00 = CustomLabel(self, str(round(Interpolation.Linear_Interpolation(self.x, self.y, self.target), 2)) )
        l01 = CustomLabel(self, str(round(Interpolation.Quadratic_Interpolation(self.x, self.y, self.target), 2)) )
        l02 = CustomLabel(self, str(round(Interpolation.Cubic_Interpolation(self.x, self.y, self.target), 2)) )
        
        l10 = CustomLabel(self, str(round(Interpolation.Linear_Lagrangian_Interpolation(self.x, self.y, self.target), 2)) )
        l11 = CustomLabel(self, str(round(Interpolation.Quadratic_Lagrangian_Interpolation(self.x, self.y, self.target), 2)) )
        l12 = CustomLabel(self, str(round(Interpolation.Cubic_Lagrangian_Interpolation(self.x, self.y, self.target), 2)) )
        
        l20 = CustomLabel(self, str(round(Interpolation.Linear_Newton_DD(self.x, self.y, self.target), 2)) )
        l21 = CustomLabel(self, str(round(Interpolation.Quadratic_Newton_DD(self.x, self.y, self.target), 2)) )
        l22 = CustomLabel(self, str(round(Interpolation.Cubic_Newton_DD(self.x, self.y, self.target), 2)) )
        
        l00.place(x=80, y = 150)
        l01.place(x=190, y = 150)
        l02.place(x=300, y = 150)
        
        l10.place(x=80, y = 200)
        l11.place(x=190, y = 200)
        l12.place(x=300, y = 200)
        
        l20.place(x=80, y = 250)
        l21.place(x=190, y = 250)
        l22.place(x=300, y = 250)
        
        
        
        
class ResultPage_Integration(ctk.CTkFrame):
    
    def __init__(self, parent):
        super().__init__(master = parent, width=600, height=400, corner_radius=10)
        self.parent = parent
        self.place(x=100, y=100)
        
        self.label0 = CustomLabel(self, 'Step size')
        self.label1 = CustomLabel(self, 'Trapezoidal')
        self.label2 = CustomLabel(self, 'Simpson')
        
        self.label0.place(x=50, y=50)
        self.label1.place(x=200, y=50)
        self.label2.place(x=350, y=50)
        results = []
        
        
    def store(self, f, a, b, n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n
    
    def compute(self):
        n = len(self.n)
        
        for i in range(n if n <= 6 else 6):
            l0 = CustomLabel(self, str(self.n[i]))
            l1 = CustomLabel(self, str(round(NI.Trapezoidal(self.f, self.a, self.b, self.n[i]), 2)))
            l2 = CustomLabel(self, str(round(NI.Simpson(self.f, self.a, self.b, self.n[i]), 2))) 
            
            l0.place(x=50, y=50 + 50*(i+1))
            l1.place(x=200, y=50 + 50*(i+1))
            l2.place(x=350, y=50 + 50*(i+1))
        

    
    
app = App("App")
app.mainloop()