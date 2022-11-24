import customtkinter as ctk
import tkinter
import ODE
import Numerical_Integration as NI

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('800x600')
        self.method = ''
        
        self.result = ResultPage(self)
        self.ODEpage = SecondPage(self)
        self.result_integration = ResultPage_Integration(self)
        self.integration = IntegrationPage(self)
        self.home = FirstPage(self)
    
    def to_result_page(self, f, x0, y0, xn, h):
        self.result.store(f, x0, y0, xn, h)
        self.result.compute()
        self.result.tkraise()
        
    def to_ODE_page(self):
        self.ODEpage.tkraise()
        
    def to_integration_page(self):
        self.integration.tkraise()
    
    def to_home(self):
        self.home.tkraise()
        
    def to_integration_result(self, f, a, b, n):
        self.result_integration.store(f, a, b, n)
        self.result_integration.compute()
        self.result_integration.tkraise()
        
        
class FirstPage(ctk.CTkFrame):
    
    def __init__(self, parent):        
        super().__init__(master = parent, width=600, height=400, corner_radius=10)
        self.parent = parent
        self.place(x=100, y=100)
        
        self.label = ctk.CTkLabel(master = self, text='Choose your method', height=40, 
            width=300, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label.place(x=150, y=30)
        
                
        self.ODE = Button(self, "Ordinary Differential Equations", lambda : parent.to_ODE_page(), 100, 90)
        self.integration = Button(self, "Numerical Integration", lambda : parent.to_integration_page(), 150, 210)     
        
        
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
        
        self.f = ctk.CTkEntry(master=self, placeholder_text="Enter the function here", width=350, height=40, 
            border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.f.place(x=50, y=70)  
        
        
        self.label1 = ctk.CTkLabel(master = self, text='x_0:', height=40, width=100, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label1.place(x=30, y=140)
        
        self.x0 = ctk.CTkEntry(master=self, placeholder_text="", width=130, height=40, border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.x0.place(x=140, y=140)  
        
        self.label2 = ctk.CTkLabel(master = self, text='y_0:', height=40, width=100, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label2.place(x=280, y=140)
        
        self.y0 = ctk.CTkEntry(master=self, placeholder_text="", width=130, height=40, border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.y0.place(x=410, y=140)  
        
        self.label3 = ctk.CTkLabel(master = self, text='x_n:', height=40, width=100, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label3.place(x=30, y=200)
        
        self.xn = ctk.CTkEntry(master=self, placeholder_text="", width=130, height=40, border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.xn.place(x=140, y=200)
        
        self.label4 = ctk.CTkLabel(master = self, text='Step size: ', height=40, width=100, corner_radius=10, text_font=("Cascadia Code", 15), bg_color='#2a2d2e')
        self.label4.place(x=280, y=200)
        
        self.h = ctk.CTkEntry(master=self, placeholder_text="", width=130, height=40, border_width=2, corner_radius=10, text_font=("Cascadia Code ExtraLight", 10))
        self.h.place(x=410, y=200)  
        
        
        self.solve = ctk.CTkButton(master = self, text='Solve', height=50, corner_radius=25, width=200,
            bg_color='#2a2d2e',text_font=("Cascadia Code ExtraLight", 13), command=self.compute)
        self.solve.place(x=200, y=300)
        
        self.back = ctk.CTkButton(master = self, text='<-', height=30, corner_radius=15, width=30,
            bg_color='#2a2d2e',text_font=("Cascadia Code ExtraLight", 10), command=lambda : parent.to_home())
        self.back.place(x=10, y=10)

    def compute(self):
        f = self.f.get()
        x0 = self.x0.get()
        y0 = self.y0.get()
        xn = self.xn.get()
        h = self.h.get()
        
        try:
            x0 = int(x0)
            print('1')
            y0 = int(y0)
            print('2')
            xn = int(xn)
            print('3')
            h = list(map(int, h.split(',')))
            from math import log, sin, cos, tan, e, pi
            eval(f.replace('y', str(y0)))
            print('ok')
            self.parent.to_result_page(f, x0, y0, xn, h)
 
        except:
            print('error')
            
class ResultPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, width=600, height=400, corner_radius=10)
        self.parent = parent
        self.place(x=100, y=100)
        
        self.label0 = CustomLabel(self, 'Step size')
        self.label1 = CustomLabel(self, 'Euler')
        self.label2 = CustomLabel(self, 'Heun')
        self.label3 = CustomLabel(self, 'Midpoint')
        self.label4 = CustomLabel(self, 'Ralston')
        
        self.label0.place(x=30, y=50)
        self.label1.place(x=150, y=50)
        self.label2.place(x=260, y=50)
        self.label3.place(x=370, y=50)
        self.label4.place(x=480, y=50)

        self.results = []
        
        
    def store(self, f, x0, y0, xn, h):
        self.f = f
        self.x0 = x0
        self.y0 = y0
        self.xn = xn
        self.h = h
    
    def compute(self):
        n = len(self.h)
        
        for i in range(n if n <= 5 else 5):
            l0 = CustomLabel(self, str(self.h[i]))
            l1 = CustomLabel(self, str(round(ODE.Euler_Method(self.f, y_0=self.y0, x_0=self.x0, x_last=self.xn, h=self.h[i]), 2)))
            l2 = CustomLabel(self, str(round(ODE.Heun(self.f, y_0=self.y0, x_0=self.x0, x_last=self.xn, h=self.h[i]), 2)))
            l3 = CustomLabel(self, str(round(ODE.Midpoint(self.f, y_0=self.y0, x_0=self.x0, x_last=self.xn, h=self.h[i]), 2)))
            l4 = CustomLabel(self, str(round(ODE.Ralston(self.f, y_0=self.y0, x_0=self.x0, x_last=self.xn, h=self.h[i]), 2)))
            
            l0.place(x=30, y=50 + 50*(i+1))
            l1.place(x=150, y=50 + 50*(i+1))
            l2.place(x=260, y=50 + 50*(i+1))
            l3.place(x=370, y=50 + 50*(i+1))
            l4.place(x=480, y=50 + 50*(i+1))
            
            self.results.append(l0)
            self.results.append(l1)
            self.results.append(l2)
            self.results.append(l3)
            self.results.append(l4)
        
        
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