from Tkinter import *
import tkFileDialog as fd
import tkMessageBox as mb
import numpy as np

import Linear_Regression_ex1


class Regression:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.grid()
        self.frame.config(width = 200, height = 150)
        #self.frame.config(relief = SUNKEN)
    def LoadFile(self):
               
        global X, y
        
        self.fname = fd.askopenfilename(filetypes=(("txt files", "*.txt;*.dat"),
                                            ("cvs files", "*.cvs"),
                                           ("All files", "*.*") ))
        self.data = np.loadtxt(self.fname, delimiter = ',')
        self.X1 = self.data[:,0]
        y = np.matrix(self.data[:,1]).T               

        m = len(y)        
        X = np.matrix([np.ones(m), self.data[:,0]]).T #add a column of ones to X

        if self.fname:
            try:
                self.reg1 = Linear_Regression_ex1.Regression()
                M = self.reg1.Matrix()                  
                
                self.label = Label(self.frame, text='Running warmUpExercise, 5x5 Indentity Matrix:')
                self.label.grid(row=0, column=0)
                self.matixLabel = Label(self.frame, text = '' if M == '' else M)
                self.matixLabel.grid(row=1, column=0, sticky='nw')
                self.reg1.Plot(self.X1, y)

            except:                     # <- naked except is a bad idea
                   mb.showerror("Open Source File", "Failed to read file\n'%s'" % self.fname)
                   
    def FitData(self):
        app = SampleApp(self.frame)
        app.mainloop()

        
        
class SampleApp(Tk):
    def __init__(self, master):
        Tk.__init__(self)
        self.frame = master
        self.label1 = Label(self, text = 'Iterations: ')
        self.label1.pack(side=LEFT)
        self.entry1 = Entry(self, width=24)
        self.entry1.pack(side=LEFT)
        
        self.label2 = Label(self, text = 'alpha: ')
        self.label2.pack(side=LEFT)
        self.entry2 = Entry(self, width=24)
        self.entry2.pack(side=LEFT)
        
        self.button = Button(self, text="Fit", command=self.on_button, width=5)
        self.button.pack(side=BOTTOM, padx = 10)

    def on_button(self):

        reg1 = Linear_Regression_ex1.Regression()
        
        linear = reg1.Linear(X, y, self.entry1.get(), self.entry2.get())
        
        Label(self.frame, text="Fitting Parameters:").grid(row=2, column=0, sticky='sw')
        Label(self.frame, text='Iterations: ').grid(row=3, column=0, sticky='sw')
        Label(self.frame, text=self.entry1.get()).grid(row=3, column=1, sticky='sw')
        Label(self.frame, text='alpha: ').grid(row=3, column=2, sticky='sw')
        Label(self.frame, text=self.entry2.get()).grid(row=3, column=3, sticky='sw')
        
        Label(self.frame, text='Fitting analysis reults: ').grid(row=4, column=0, sticky='sw')
        label1 = Label(self.frame, text = 'Cost: ')
        label1.grid(row=5, column=0, sticky='sw')
        costLabel = Label(self.frame, text = '' if linear == '' else float(linear[0]))
        costLabel.grid(row=5, column=1, sticky='sw')
        Label(self.frame, text='Theta: ').grid(row=6, column=0, sticky='sw')
        Label(self.frame, text='' if linear == '' else float(linear[1])).grid(row=6, column=1, sticky='sw')
        Label(self.frame, text='' if linear == '' else float(linear[2])).grid(row=6, column=2, sticky='sw')
        
class Gui:
    
    def __init__(self, master):

        buildMenu = Menu()
        
        master.config(menu=buildMenu)
        
        reg = Regression(master)
        
        
        subMenu = Menu(buildMenu)
        buildMenu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Open", command=reg.LoadFile)
        subMenu.add_command(label="New", command=reg.LoadFile)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=reg.LoadFile)
        
        editMenu=Menu(buildMenu)
        buildMenu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Fit", command=reg.FitData)        


if __name__ == "__main__":     
    root = Tk()
    root.wm_title("Linear Regression")
    gui = Gui(root)
    root.mainloop()