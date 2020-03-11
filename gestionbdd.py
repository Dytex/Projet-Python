import sqlite3





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


def insertVaribleIntoTable():
    """
        Permet d'insérer dans une table
    """
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
        print("Python Variables inserted successfully into user table")
    
        cursor.close()
    
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
    
    
"""Permet d'afficher les élèves"""
def display_student():
    try:
        sqliteConnection = sqlite3.connect('bdd.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        
        sqlite_select = """SELECT * FROM user;"""
    
        
        cursor.execute(sqlite_select)
        sqliteConnection.commit()
        resultats = cursor.fetchall()
        for resultat in resultats:
            print(resultat)
    
        cursor.close()
    
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
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
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO user1
                                  (nom, prenom, photo) VALUES (?, ?, ?)"""

        empPhoto = convertToBinaryData(photo)
        
        # Convert data into tuple format
        data_tuple = (name, prenom, empPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")


    
    
if __name__ == "__main__":
    
