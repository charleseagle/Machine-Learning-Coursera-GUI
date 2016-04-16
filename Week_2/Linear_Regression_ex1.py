from __future__ import division
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
import ttk   
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 


#from matplotlib import cm
import numpy as np
import warmUpExercise, computeCost, gradientDescent


class PlotFig(Tk.Frame):
    def __init__(self, root, f):
        Tk.Frame.__init__(self, root)
        
        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(f, root)
        canvas.show()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        
        toolbar = NavigationToolbar2TkAgg(canvas, root)
        toolbar.update()
        canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        
        
        def on_key_event(event):
            print('you pressed %s' % event.key)
            key_press_handler(event, canvas, toolbar)
        
        canvas.mpl_connect('key_press_event', on_key_event)
        
        
        def _quit():
            root.quit()     # stops mainloop
            root.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
        button = Tk.Button(root, text='Quit', command=_quit)
        button.pack(side=Tk.BOTTOM)

        

class Regression():
    def Matrix(self): 
        matrix = warmUpExercise.warmUpExercise()
        return matrix
        
    def Plot(self, X, y):
        
        root = Tk.Tk()
        root.wm_title("Scatter Plot")
        
        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)
        
        a.plot(X, y, 'o')
        a.set_title('Raw data')
        a.set_xlabel('population')
        a.set_ylabel('Profit')
        
        PlotFig(root, f).mainloop()


        
    def Linear(self, X, y, iters, alp):        
       

        theta = np.matrix(np.zeros(2)).T #initialize fitting parameters

        # gradient descent setting
        iterations = int(iters)
        alpha = float(alp)
        
        # compute and display initial cost
        J = computeCost.computeCost(X, y, theta)
        # Run gradietn descent
        self.theta, J_hisotry = gradientDescent.gradientDescent(X, y, theta, alpha, iterations)
        
        # Print theta to screen
        
        root = Tk.Tk()
        root.wm_title("Linear Fit Plot")
        
      
        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)

        a.plot(X[:,1], y, 'o', label = 'Training data', color = 'blue')
        a.plot(X[:,1], X*self.theta, '-', label = 'Linear regression', color = 'red')
        a.legend(loc = 4)
        a.set_title('Linear fitting')
        a.set_xlabel('population')
        a.set_ylabel('Profit')
        #a.text(7, 20, 'Initial cost: %s \n Theta: %s '  % (J[0,0], self.theta))
        PlotFig(root, f).mainloop()        
        return [J, self.theta[0], self.theta[1]]
        
    def Prediction(self):
        #Predict values for population sizes of 35,000 and 70,000
        predict1 = [1, 3.5]*self.theta
        print 'For population = 35,000, we predict a profit of ', predict1*1000
        predict2 = [1, 7]*self.theta
        print "For population = 70,000, we predict a profit of", predict2*10000
        

        # Visualizing J(theta_0, theta_1)
        print "Visualizing J(theta_0, theta_1)"
        
        theta0_vals = np.linspace(-10, 10, 100)
        theta1_vals = np.linspace(-1, 4, 100)
        
        J_vals = np.zeros((len(theta0_vals), len(theta1_vals)))
        
        for i in range(len(theta0_vals)):
            for j in range(len(theta1_vals)):
                t = np.matrix([theta0_vals[i], theta1_vals[j]]).T
                J_vals[i,j] = computeCost.computeCost(self.X, self.y, t)
        # transpose J_vals
        J_vals = J_vals.T
        
        #surface plot
        root = Tk.Tk()
        root.wm_title("Scatter Plot")
        


        
      
        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)
        
        a.contour(theta0_vals, theta1_vals, J_vals, np.logspace(-2, 3, 20))
        a.xlabel('theta_0')
        a.ylabel('theta_1')

        
        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.show()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        
        toolbar = NavigationToolbar2TkAgg(canvas, root)
        toolbar.update()
        canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        
        
        def on_key_event(event):
            print('you pressed %s' % event.key)
            key_press_handler(event, canvas, toolbar)
        
        canvas.mpl_connect('key_press_event', on_key_event)
        
        
        def _quit():
            root.quit()     # stops mainloop
            root.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
        button = Tk.Button(master=root, text='Quit', command=_quit)
        button.pack(side=Tk.BOTTOM)
        
        Tk.mainloop()   
        

        ax = Axes3D(a)
        #ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(theta0_vals, theta1_vals, J_vals)
        ax.set_xlabel('theta_0')
        ax.set_ylabel('theta_1')
        ax.set_zlabel('J Values')
        





