from DBconnection import DBconnection

class DataAccess(DBconnection):
    def accessUrl(self):
        db = DBconnection().getConnection()
        cursor = db.cursor(buffered=True)
        query = ("SELECT url FROM country")
        cursor.execute(query)
        urls = cursor.fetchall()
        cursor.close()
        db.close()
        for link in urls:
            page = ''.join(link)     
            yield page 

