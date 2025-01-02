from tkinter import * 
class UI:
    def __init__(self,root):
        self.root = root
        self.root.title("App")
        self.root.geometry("300x300")
        self.root.configure(background="lightblue")

    def main_menu(self,buttonOrder,buttonExit,buttonSave):
        buttonOrder.grid(row=0,column=1,padx=110,pady=10)
        buttonExit.grid(row=1,column=1,padx=100,pady=10)
        buttonSave.grid(row=2,column=1,padx=100,pady=10)
