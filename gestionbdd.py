import sqlite3


con = sqlite3.connect('bdd.db')
"""Permet de supprimer une table"""
def drop_table():
    cur = con.cursor()
    x = str(input('Veuillez entrer le nom de la table\n'))
    cur.execute('drop table '+ x)
    
    print('La table a bien été supprimé\n')
""" Permet de créer une table"""
def create_table():
    cur = con.cursor()
    x = str(input('Veuillez rentrer le nom de la table\n'))
    cur.execute('create table '+ x)
    con.commit()
    print('La table a bien été créée')
    
"""Permet d'insérer dans une table"""
def insertVaribleIntoTable():
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
    
    
if __name__ == "__main__":
    
