import mysql.connector


class DBconnection(): 
    def getConnection(self): 
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password13",
            database = "coins"
        )
        return db