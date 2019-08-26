import MySQLdb
import MySQLdb.cursors

'''
dbpool = adbapi.ConnectionPool('MySQLdb',
            host = '192.168.2.2',
            db = 'dbname',
            user = 'root',
            passwd = 'root',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True)
'''

import time

print( time.time())
#print(time.strftime())
sd ='1234567abcdefg'.encode('utf-8')
print(type(sd))
print(sd[3::])
print( time.strftime('%Y-%m-%d %H:%M:%S') )
print( time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) )