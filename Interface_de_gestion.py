import tkinter

#FENETRE PRINCIPALE
page = tkinter.Tk()
page.title("MENU PRINCIPALE")
largeur_page = page.winfo_screenwidth()
hauteur_page = page.winfo_screenheight()
page.geometry(f"{largeur_page}x{hauteur_page}")
page.resizable(False,False)


#TITRE
titre = tkinter.Label(page , text="GESTION NOTES DES ETUDIANTS" , bg="#000000" , fg="#FFFFFF" ,
                       font=("sans serif", 20) , relief="sunken" , borderwidth=3 )

lbl_matricule = tkinter.Label(text="MATRICULE")
saisi_matricule = tkinter.Entry(page)

lbl_nom = tkinter.Label(text="NOM")
saisi_nom = tkinter.Entry(page)

lbl_prenom = tkinter.Label(text="PRENOM")
saisi_prenom = tkinter.Entry(page)

lbl_classe = tkinter.Label(text="CLASSE")
saisi_classe = tkinter.Entry(page)

lbl_matiere = tkinter.Label(text="MATIERE")
saisi_matiere = tkinter.Entry(page)

lbl_note = tkinter.Label(text="NOTE")
saisi_note = tkinter.Entry(page)

btn_enregistrer = tkinter.Button(page , text="Eregistrer")
btn_modifier = tkinter.Button(page , text="Modifier")
btn_supprimer = tkinter.Button(page , text="Supprimer")

titre.place(x=0 , y=0 , width=largeur_page , height=80)

lbl_matricule.place(x=70 , y=150)
saisi_matricule.place(x=250 , y=150)

lbl_nom.place(x=70 , y=200 )
saisi_nom.place(x=250 , y=200 )

lbl_prenom.place(x=70 , y=250)
saisi_prenom.place(x=250 , y=250)

lbl_classe.place(x=70 , y=350 )
saisi_classe.place(x=250 , y=350 )

lbl_matiere.place(x=70 , y=400)
saisi_matiere.place(x=250 , y=400)

lbl_note.place(x=70 , y=450)
saisi_note.place(x=250 , y=450)

btn_enregistrer.place(x=250 , y=500)
btn_modifier.place(x=250 , y=550)
btn_supprimer.place(x=250 , y=600)

page.mainloop()