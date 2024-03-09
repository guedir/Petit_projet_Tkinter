import tkinter
from tkinter import ttk

#FENETRE PRINCIPALE
page = tkinter.Tk()
page.title("MENU PRINCIPALE")
largeur_page = page.winfo_screenwidth()
hauteur_page = page.winfo_screenheight()
page.geometry(f"{largeur_page}x{hauteur_page}")
page.resizable(False,False)
page.configure(bg="#091821")

#LABEL TITRE
titre = tkinter.Label(page , text="GESTION NOTES DES ETUDIANTS" , bg="#2F4F4F" , fg="#FFFAFA" ,
                       font=("sans serif", 20) , relief="sunken" , bd=3 )
titre.place(x=0 , y=0 , width=largeur_page , height=80)

#LABEL MATRICULE
lbl_matricule = tkinter.Label(page, text="MATRICULE" , font=("arial",15) , bg="#091821" , fg="#FFFFFF")
saisi_matricule = tkinter.Entry(page , bd=4, font=("Arial" , 15) )
lbl_matricule.place(x=70 , y=150)
saisi_matricule.place(x=250 , y=150 , width=150)

#LABEL NOM
lbl_nom = tkinter.Label(page, text="NOM" , font=("arial",15) , bg="#091821" , fg="#FFFFFF")
saisi_nom = tkinter.Entry(page, bd=4, font=("Arial" , 15))
lbl_nom.place(x=70 , y=200  )
saisi_nom.place(x=250 , y=200 )

#LABEL PRENOM
lbl_prenom = tkinter.Label(page, text="PRENOM" , font=("arial",15) , bg="#091821" , fg="#FFFFFF")
saisi_prenom = tkinter.Entry(page, bd=4, font=("Arial" , 15))
lbl_prenom.place(x=70 , y=250 )
saisi_prenom.place(x=250 , y=250)

#SEXE ELEVE
valeursexe= tkinter.StringVar()
sexe_masculin = tkinter.Radiobutton(page, text="MASCULIN", bg="#091821", fg="#696969",font=("arial",14), value="M",
                                    variable=valeursexe, indicatoron=0 )
sexe_feminin = tkinter.Radiobutton(page , text="FEMININ", bg="#091821", fg="#696969", font=("arial",14), value="F",
                                    variable=valeursexe, indicatoron=0)
sexe_masculin.place(x=250 , y=300, width=100)
sexe_feminin.place(x=380 , y=300, width=100)

#LABEL CLASSE
lbl_classe = tkinter.Label(page, text="CLASSE" , font=("arial",15) , bg="#091821" , fg="#FFFFFF")
lbl_classe.place(x=70 , y=350 )
option = ["CP" , "CE1" , "CE2" , "CM1" , "CM2" , "6e" , "5e" , "4e" , "3e"]
option_selected = tkinter.StringVar()
combo = ttk.Combobox(page, font=("Arial" , 14), textvariable=option_selected, values=option)
combo.place(x=250 , y=350 , width=100 )

#LABEL MATIERE
lbl_matiere = tkinter.Label(page, text="MATIERE" , font=("arial",15) , bg="#091821" , fg="#FFFFFF")
saisi_matiere = tkinter.Entry(page, bd=4, font=("Arial" , 15))
lbl_matiere.place(x=70 , y=400)
saisi_matiere.place(x=250 , y=400)

#LABEL NOTE
lbl_note = tkinter.Label(page, text="NOTE" , font=("arial",15) , bg="#091821" , fg="#FFFFFF")
saisi_note = tkinter.Entry(page, bd=4, font=("Arial" , 15))
lbl_note.place(x=70 , y=450)
saisi_note.place(x=250 , y=450, width=120)

#BOUTTONS
btn_enregistrer = tkinter.Button(page , text="Eregistrer" , bg="#FF4500" , fg="#FFFFFF", font=("Arial",10,"bold"), bd=4)
btn_modifier = tkinter.Button(page , text="Modifier", bg="#FF4500" , fg="#FFFFFF", font=("Arial",10,"bold"), bd=4)
btn_supprimer = tkinter.Button(page , text="Supprimer", bg="#FF4500" , fg="#FFFFFF", font=("Arial",10,"bold"), bd=4)
btn_enregistrer.place(x=250 , y=500, width=120)
btn_modifier.place(x=250 , y=550, width=120)
btn_supprimer.place(x=250 , y=600, width=120)

#TABLE
table = ttk.Treeview(page , columns=(1,2,3,4,5,6,7), show="headings", height=5)
table.place(x=520 , y=150 , width=780 ,height=500)

#ENTETE
table.heading(1 , text="MAT")
table.heading(2 , text="NOM")
table.heading(3 , text="PRENOM")
table.heading(4 , text="SEXE")
table.heading(5 , text="CLASSE")
table.heading(6 , text="MATIERE")
table.heading(7 , text="NOTE")

table.column(1, width=30)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=30)
table.column(5, width=30)
table.column(6, width=100)
table.column(7, width=30)

page.mainloop()