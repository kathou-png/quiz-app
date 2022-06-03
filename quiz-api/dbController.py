import sqlite3

#used to interact with db
def initDbConnection():
    db_conn=sqlite3.connect("..\\bdd.db")
    db_conn.isolation_level = None
    #créée le curseur
    cur = db_conn.cursor()
    return cur
