import tkinter

#Fenetre de connection
fenetre = tkinter.Tk()
fenetre.title("FENETRE DE CONNECTION")
fenetre.resizable(False,False)
fenetre.geometry("300x200")

#Formulaire
titre = tkinter.Label(text="Formulaire de connexion")
user = tkinter.Label(text="Nom Utilisateur :")
zone_saisi1 = tkinter.Entry()
mp = tkinter.Label(text="Mot de Passe :")
zone_saisi2 = tkinter.Entry()
btn = tkinter.Button(text="Connexion")

titre.place(x=0 , y=0 , width=300)
user.place(x=10 , y=60 )
zone_saisi1.place(x=120 , y=60 , width=150)
mp.place(x=20 , y=90 )
zone_saisi2.place(x=120 , y=90 , width=150)
btn.place(x=120 , y=120 , width=150)

fenetre.mainloop()