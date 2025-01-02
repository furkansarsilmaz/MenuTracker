from tkinter import * 
class UI:
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
    def main_menu(self):
        self.clear_screen()
        self.buttonOrder = Button(self.root,text="Order",width=5,font=("arial",12,"italic"),command= self.getTable)
        self.buttonOrder.grid(row=0,column=1,padx=110,pady=10)

        self.buttonExit = Button(self.root,text="Exit",width=5,font=("arial",12,"italic"),command= self.exit_App)
        self.buttonExit.grid(row=1,column=1,padx=100,pady=10)

        self.buttonSave = Button(self.root,text="Save",width=5,font=("arial",12,"italic"),command= self.saveDay)
        self.buttonSave.grid(row=2,column=1,padx=100,pady=10)