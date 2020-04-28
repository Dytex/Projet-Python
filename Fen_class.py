# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:00:28 2020

@author: gateb
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:24:46 2020

@author: gateb
"""

# -*- coding: utf-8 -*-


from tkinter import * 
from tkinter.messagebox import *
from face_detection import *

def Lancement():     

    fenetre = Tk()
    fenetre.title('page 1')
    fenetre.geometry("300x350")
    fenetre.configure(bg='white')
    fenetre.resizable(False, False)
    
    def callback():
        
        if askyesno('Lancement', 'Voulez-vous lancer la reconnaissance faciale ?'):
            write_slogan()
        else:
            showinfo('Refus','Vous allez etre redirigé vers la sortie...')
            showerror("Aha", "Ce fut un plaisir")
            fenetre.destroy()
                      
    def write_slogan():
        fenetre.destroy()
        
        # webcam_face_recognizer(db)
        fen = Tk()
        fen.geometry("500x550")
        fen.configure(bg='white')
        fen.resizable(False, False)
        label = Label(fen, bg='white', text="Bachelor 1")
        label.grid(row=0, column=2)
        bou_g1 = Button(fen, width=20, height=2, text="Groupe 1", background="white", command=lambda:groupe1(fen))
        bou_g1.grid(row=1, column=1, padx=40, pady=250)
        bou_g2 = Button(fen, width=20, height=2, text="Groupe 2", background="white", command=lambda:groupe2(fen))
        bou_g2.grid(row=1, column=3)
        
        
        fen.mainloop()
    #FENETRE START
    # canvas Start
        
    def groupe1(fenetre):
        fenetre.destroy()
        
        LancementFaceReco()
        
 


    def groupe2(fenetre):
        fenetre.destroy()
        
        LancementFaceReco()
 
    
    
    
    
    bou_start = Button(fenetre ,width=43, height=2, relief=FLAT, text="Start", background='white', command=callback)

    bou_start.place(relx=0, rely=0.4)
    bouton=Button(fenetre, text="Fermer", width=43, relief=FLAT, background='white', command=fenetre.destroy)
    bouton.place(relx=0, rely=0.92)
    
    
   
    
    
  
    # bouton de sortie
    
    
    

    fenetre.mainloop()
if __name__ == "__main__":
    Lancement()
    

    
    