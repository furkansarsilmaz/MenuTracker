from tkinter import * 
from tkinter import messagebox
from UI import UI 
import sys
import csv 

class App:
    def __init__(self,root):
        self.root = root
        self.ui = UI(self.root)
        self.menu = {
            "Kebab": 0 ,
            "Doner": 0,
            "Baklava":0,
            "Turkish coffee":0
        }
        self.buttonOrder = Button(self.root,text="Order",width=5,font=("arial",12,"italic"),command= self.getTable)
        self.buttonExit = Button(self.root,text="Exit",width=5,font=("arial",12,"italic"),command= self.exit_App)
        self.buttonSave = Button(self.root,text="Save",width=5,font=("arial",12,"italic"),command= self.saveDay)
        self.ui.main_menu(self.buttonOrder,self.buttonExit,self.buttonSave)

    def getTable(self):
        self.clear_screen()
        row_num = 0
        column_num = 0 
        table_num = ""
        for i in range(10):
            Button(self.root,text=i,width=4,height=3,
            command= lambda i=i : self.getOrder(i)).grid(row=row_num,column=column_num,padx=30,pady=20)
            column_num += 1 
            if column_num == 3 :
                row_num += 1 
                column_num = 0 


    def getOrder(self,table):
        """
        Clears the screen and creates a new one with loop.
        """
        self.clear_screen()
        row_num = 0
        for i in self.menu.keys():
            # Menu 
            Label(self.root,text=i).grid(row= row_num , column=0 ,padx=20,pady=10)
            
            # Quantity
            Label(self.root,text=self.menu[i]).grid(row= row_num , column= 1)
            
            # Increase Quantity
            Button(self.root,text="+",width=2,command = lambda i=i : self.plus_quantity(i,table)).grid(row= row_num , column= 2,padx=10)
            
            # Decrease Quantity
            Button(self.root,text="-",width=2,command=lambda i=i : self.minus_quantity(i,table)).grid(row=row_num,column= 3,padx=10)
            row_num += 1
        
        table_num = Label(self.root,text="Table number :"+str(table))
        table_num.grid(row=4,column=2,pady=10)
        backButton = Button(self.root,text="Back",command=self.main_menu)
        backButton.grid(row=5,column=2,pady=10)

    def saveDay(self):
        with open("orders.csv","w",newline="") as csvfile :
            Writer = csv.writer(csvfile)
            Writer.writerow(["Order","Quantity"])
            for item,quantity in self.menu.items():
                Writer.writerow([item,quantity])
        messagebox.showinfo("Succeed","Orders saved")

    def minus_quantity(self,item,table):
        if self.menu[item] <= 0 :
            pass
        else:
            self.menu[item] -= 1
        self.getOrder(table)

    def plus_quantity(self,item,table):
        self.menu[item] += 1
        self.getOrder(table)

    def clear_screen(self):
        for i in self.root.winfo_children():
            i.destroy()

    def exit_App(self):
        if messagebox.askyesno("Exit","Do you want to exit ?"):
            sys.exit()

if __name__ == "__main__":
    root = Tk()
    App(root)
    root.mainloop()
    root.winfo_children