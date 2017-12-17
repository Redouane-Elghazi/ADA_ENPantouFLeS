from tkinter import *

class Interface(Frame):
    def __init__(self, fenetre, liste, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)

        self.grid(sticky=N+S+E+W)
        
        self.gen = (val for val in liste)
        self.yes_l = []
        self.no_l = []
        self.cur = next(self.gen)
        # Création de nos widgets
        self.word = Label(self, text=self.cur)
        self.word.grid(row=0,column=0,columnspan=2)

        self.bouton_yes = Button(fenetre,text="Yes",command=self.yes)
        self.bouton_yes.grid(row=1,column=1,sticky=E+W)
        
        self.bouton_no = Button(fenetre,text="No",command=self.no)
        self.bouton_no.grid(row=1,column=0,sticky=E+W)
        
        self.bouton_exit = Button(fenetre,text="Save",command=self.quit)
        self.bouton_exit.grid(row=2,column=0,columnspan=2)
        
    def yes(self):
        self.yes_l.append(self.cur)
        self.cur = next(self.gen)
        self.word['text'] = self.cur
        
    def no(self):
        self.no_l.append(self.cur)
        self.cur = next(self.gen)
        self.word['text'] = self.cur
