import MySQLdb
Con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="yoruname", passwd="yourpwd", db="test")
Cursor = Con.cursor()
sql = "SELECT * FROM test.testing"
Cursor.execute(sql)