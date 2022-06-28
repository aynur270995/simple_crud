import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)
        

def create_table(con):
    cursorObj= con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS person(id integer PRIMARY KEY, name text, surname text, age integer, address text, position text, active integer )")
    con.commit()
    print("Cədvəl yaradılmışdır.")

def insert(con, entites):
    cursorObj= con.cursor()
    cursorObj.execute('INSERT INTO person(id, name, surname, age, address, position, active) VALUES(?, ?, ?, ?, ?, ?, ?)', entites)
    con.commit()
    print("Melumatlariniz cedvele elave olundu..")



def select(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM person')

    rows = cursorObj.fetchall()
    return rows


def update (con, e):
    cursorObj = con.cursor()
    cursorObj.execute("UPDATE person SET name = ?, surname = ?, age = ? , address =?, position=?, active=? where id = ?",e)
    con.commit()


def delete(con, id):
    cursorObj= con.cursor()
    cursorObj.execute('DELETE FROM person WHERE id=?', (id,))
    con.commit()
    

def select_by_Id(con, id):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM person WHERE id=?", (id,))

    rows = cursorObj.fetchall()
    return rows 

    
if __name__== "__main__":
    con = create_connection()
    create_table(con)
    #entities = (2, "Aynur", "Aliyeva", 26, "Baku", "Muhasib")
    #insert(con, entities)
    #select(con)
    #update_data = ("Aynure", "Isayeva", 33, "Baki", "resepion", 1, 1)
    #pdate(con, update_data)
    
