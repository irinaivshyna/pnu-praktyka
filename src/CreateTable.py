from DBconnection import DBconnection

class CreateTable(DBconnection):
    def createTable(self):
        db = DBconnection().getConnection()
        cursor = db.cursor(buffered=True)
        query = (
            "CREATE TABLE IF NOT EXISTS `coins`.`coin` (`id` int unsigned NOT NULL AUTO_INCREMENT,`title` varchar(511) NOT NULL,`url` varchar(511) NOT NULL,`country_id` int unsigned NOT NULL,PRIMARY KEY (`id`),KEY `country_id` (`country_id`),CONSTRAINT `coin_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;"
        )
        cursor.execute(query)
        db.commit()
        cursor.close()
        db.close()