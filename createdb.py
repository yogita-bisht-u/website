import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT Exists COURSE(cid INTEGER PRIMARY KEY AUTOINCREMAENT,name text,duration text,charges text,description text)")   
    con.commit()
    create_db()
    