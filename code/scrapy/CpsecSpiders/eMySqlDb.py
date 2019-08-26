import MySQLdb
Con = MySQLdb.Connect(host="localhost", port=3306, user="csy_lg", passwd="123456", db="test_db",
       )
Cursor = Con.cursor()
#sql = "SELECT * FROM test.testing"
#Cursor.execute(sql)


sql = "create database tianya_db DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;"
Cursor.execute(sql)
Cursor.fetchall()
sql = """use tianya_db;
CREATE TABLE article_info (
    id INT (13) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    article_name CHAR (150),
    article_time CHAR (30),
    article_url CHAR (100), 
    crawl_time CHAR (30), 
    praise_num CHAR (30), 
    comment_num CHAR (30),
article_from CHAR (30),
article_author CHAR (30)
);"""
Cursor.execute(sql)
Cursor.fetchall()
# Con.commit()

sql3 = """
use tianya_db;
CREATE TABLE article_content (
    id INT (13) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    article_content TEXT(2)
); """
cs = Cursor.execute(sql3)
print(cs)
Con.commit()
Con.close()

