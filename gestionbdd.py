# -*- coding: utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(host="localhost", user="benjamin",password="EpsiEpsi", database="test1")
cursor = conn.cursor()
conn.close()

if __name__ == '__main__':
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS visiteurs (
        id int(5) NOT NULL AUTO_INCREMENT,
        name varchar(50) DEFAULT NULL,
        age INTEGER DEFAULT NULL,
        PRIMARY KEY(id)
    );
    """)
    
    user = ("olivier", "34")
    cursor.execute("""INSERT INTO users (name, age) VALUES(%s, %s)""", user)
    
    cursor.execute("""SELECT id, name, age FROM users WHERE id = %s""", ("5", ))
    rows = cursor.fetchall()
    for row in rows:
        print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))