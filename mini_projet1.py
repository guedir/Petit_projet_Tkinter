import tkinter
from tkinter import messagebox

def SeConnecter():
    champ1 = zone_saisi1.get()
    champ2 = zone_saisi2.get()
    if (champ1 == "") and (champ2 == ""):
        messagebox.showerror("Erreur","veuillez remplire les champs")
        zone_saisi1.delete("0","end")
        zone_saisi2.delete("0","end")
    elif champ1 == "admin" and champ2 == "0000":
        messagebox.showinfo("connecté","bienvenue")
        zone_saisi1.delete("0","end")
        zone_saisi2.delete("0","end")
        fenetre.destroy()
    else:
        messagebox.showwarning("Attention" , "Nom utilisateur ou Mot de passe incorrecte")
        zone_saisi1.delete("0","end")
        zone_saisi2.delete("0","end")
    
#Fenetre de connexion
fenetre = tkinter.Tk()
fenetre.title("FENETRE DE CONNEXION")
fenetre.resizable(False,False)
fenetre.geometry("300x200")
fenetre.configure(bg="#091821")

#Formulaire
titre = tkinter.Label(fenetre , text="Formulaire de connexion" , bg="#000000" , fg="#FFFFFF" , font=("sans serif" , 18))
user = tkinter.Label(fenetre , text="Nom Utilisateur :" ,  bg="#091821" , fg="#FFFFFF" , font=("",10,"bold"))
zone_saisi1 = tkinter.Entry(fenetre , bd=2)
mp = tkinter.Label(fenetre , text="Mot de Passe :" , bg="#091821" , fg="#FFFFFF", font=("",10,"bold"))
zone_saisi2 = tkinter.Entry(fenetre , show="*" , bd=2)
btn = tkinter.Button(fenetre,text="Connexion",bg="#FF4500",fg="white",font=("Arial",10,"bold"),bd=3,command=SeConnecter)

#Placement des Widgets
titre.place(x=0 , y=0 , width=300)
user.place(x=10 , y=60 )
zone_saisi1.place(x=120 , y=60 , width=150)
mp.place(x=20 , y=90 )
zone_saisi2.place(x=120 , y=90 , width=150)
btn.place(x=120 , y=120 , width=150)

fenetre.mainloop()