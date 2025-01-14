from tkinter import * 
from tkinter import messagebox 
import sys
import csv 
class App:
    def __init__(self,root):
        self.root = root
        self.root.title("App")
        self.root.geometry("300x300")
        self.root.configure(background="lightblue")
        self.menu = {
            "Kebab": 0 ,
            "Doner": 0,
            "Baklava":0,
            "Turkish coffee":0
        }
        self.main_menu()

    def main_menu(self):
        self.clear_screen()
        self.buttonOrder = Button(self.root,text="Order",width=5,font=("arial",12,"italic"),command= self.getOrder)
        self.buttonOrder.grid(row=0,column=1,padx=110,pady=10)

        self.buttonExit = Button(self.root,text="Exit",width=5,font=("arial",12,"italic"),command= self.exit_App)
        self.buttonExit.grid(row=1,column=1,padx=100,pady=10)

        self.buttonSave = Button(self.root,text="Save",width=5,font=("arial",12,"italic"),command= self.saveDay)
        self.buttonSave.grid(row=2,column=1,padx=100,pady=10)
    
    def getOrder(self):
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
            Button(self.root,text="+",width=2,command = lambda i=i : self.plus_quantity(i)).grid(row= row_num , column= 2,padx=10)
            
            # Decrease Quantity
            Button(self.root,text="-",width=2,command=lambda i=i : self.minus_quantity(i)).grid(row=row_num,column= 3,padx=10)
            row_num += 1

        backButton = Button(self.root,text="Back",command=self.main_menu)
        backButton.grid(row=4,column=2)

    def saveDay(self):
        with open("orders.csv","w",newline="") as csvfile :
            Writer = csv.writer(csvfile)
            Writer.writerow(["Order","Quantity"])
            for item,quantity in self.menu.items():
                Writer.writerow([item,quantity])
        messagebox.showinfo("Succeed","Orders saved")

    def minus_quantity(self,item):
        if self.menu[item] <= 0 :
            pass
        else:
            self.menu[item] -= 1
        self.getOrder()

    def exit_App(self):
        if messagebox.askyesno("Exit","Do you want to exit ?"):
            sys.exit()

    def plus_quantity(self,item):
        self.menu[item] += 1
        self.getOrder()

    def clear_screen(self):
        for i in self.root.winfo_children():
            i.destroy()


if __name__ == "__main__":
    root = Tk()
    App(root)
    root.mainloop()
    root.winfo_children