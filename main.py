import sqlite3
from tkinter import *
from tkinter.messagebox import * # boîte de dialogue


def drop_table():
    """
        Permet de supprimer une table
    """

    try:
        sqliteConnection = sqlite3.connect('bdd.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")


        nom_table = str(input('Veuillez entrer le nom de la table\n'))
        cursor.execute('drop table '+ nom_table)
        sqliteConnection.commit()
        print("La table a bien été supprimée")

        cursor.close()

    except sqlite3.Error as error:
        print("Error", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


def create_table():
    """
        Permet de créer une table
    """

    try:
        sqliteConnection = sqlite3.connect('bdd.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")


        nom_table = str(input('Veuillez rentrer le nom de la table\n'))
        cursor.execute('create table '+ nom_table)
        sqliteConnection.commit()
        print("La table a bien été créée")

        cursor.close()

    except sqlite3.Error as error:
        print("Error", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


def insert_table():
    """
        Permet d'insérer dans une table
    """
    fenetre = Tk()
    try:
        sqliteConnection = sqlite3.connect('bdd.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        nom = str(input('Veuillez entrer le nom de l\élève\n'))
        prenom = str(input('Veuillez entrer le prenom de l`\élève\n'))
        sqlite_insert = """INSERT INTO user
                          (nom,prenom)
                          VALUES (?, ?);"""

        data_tuple = (nom, prenom)
        cursor.execute(sqlite_insert, data_tuple)
        sqliteConnection.commit()
        print("Insertion validée")
        print(nom + " " + prenom + " a bien été ajouté")

        cursor.close()

    except sqlite3.Error as error:
        print("Erreur de l\insertion dans la table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


"""Permet d'afficher les élèves"""
def display_student():
    try:
        sqliteConnection = sqlite3.connect('bdd.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite\n")
        print("Voici la liste des images\n")

        sqlite_select = """SELECT * FROM user;"""


        cursor.execute(sqlite_select)
        sqliteConnection.commit()
        resultats = cursor.fetchall()
        for resultat in resultats:
            print(resultat)
            return(resultat)

        cursor.close()

    except sqlite3.Error as error:
        print("Erreur sur l'affichage des élèves", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def convertToBinaryData(filename):
    """
        Permet de convertir une image en binaire
    """

    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insert_image(name, prenom, photo):
    """
        Permet d'insérer une image dans la base de donnée en renseignant le nom et prénom de l'élève
    """

    try:
        sqliteConnection = sqlite3.connect('bdd.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite\n")

        sqlite_insert_blob_query = """ INSERT INTO user1
                                  (nom, prenom, photo) VALUES (?, ?, ?)"""

        empPhoto = convertToBinaryData(photo)


        data_tuple = (name, prenom, empPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("L\élève a bien été enregistré avec sa photo")
        cursor.close()

    except sqlite3.Error as error:
        print("Erreur pour insérer l\élève", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")
def Verification():
    if Login.get() == 'Benjamin@gmail.com':
        # le mot de passe est bon : on affiche une boîte de dialogue puis on ferme la fenêtre
        showinfo('Résultat','Vous pouvez accèder a l application.\nAu revoir !')
        Mafenetre.destroy()
    else:
        # le mot de passe est incorrect : on affiche une boîte de dialogue
        showwarning('Résultat','Vous n avez pas été trouvé dans la base de donnée.\nVeuillez recommencer !')
        Login.set('')

if __name__ == "__main__":





    # Création de la fenêtre principale (main window)
    Mafenetre = Tk()
    Mafenetre.title('Identification requise')

    # Création d'un widget Label (texte 'Mot de passe')
    Label1 = Label(Mafenetre, text = 'Login ')
    Label1.pack(side = LEFT, padx = 5, pady = 5)

    # Création d'un widget Entry (champ de saisie)
    Login= StringVar()
    Champ = Entry(Mafenetre, textvariable= Login, show='*', bg ='bisque', fg='maroon')
    Champ.focus_set()
    Champ.pack(side = LEFT, padx = 5, pady = 5)

    # Création d'un widget Button (bouton Valider)
    Bouton = Button(Mafenetre, text ='Valider', command = Verification)
    Bouton.pack(side = LEFT, padx = 5, pady = 5)
    Bouton2 = Button(Mafenetre, text ='Voir les élèves', command = display_student)
    Bouton2.pack(side = RIGHT, padx = 5, pady = 5)
    print(Login)
    Mafenetre.mainloop()
