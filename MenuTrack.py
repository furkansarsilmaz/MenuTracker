from tkinter import * 
class App:
    def __init__(self,root):
        self.root = root
        self.root.title("App")
        self.root.geometry("300x300")

        self.buttonOrder = Button(self.root,text="Order",command=self.getOrder)
        self.buttonOrder.pack(pady=10)

        self.menu = {
            "Kebab": 0 ,
            "Doner": 1,
            "Baklava":3
        }
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

    def minus_quantity(self,item):
        if self.menu[item] <= 0 :
            pass
        else:
            self.menu[item] -= 1
        self.getOrder()


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