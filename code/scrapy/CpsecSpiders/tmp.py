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
def timeDemo():
    import time

    print( time.time())
    #print(time.strftime())
    sd ='1234567abcdefg'.encode('utf-8')
    print(type(sd))
    print(sd[3::])
    print( time.strftime('%Y-%m-%d %H:%M:%S') )
    print( time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) )

a=[1,2,3,'d']
ss= "%s,%s,%d,%s" % (a[0],a[1],a[2],a[3])
print(ss)

import hashlib
st = "werwerwerer35"
md5 = hashlib.md5()
md5.update(st.encode('utf-8'))     #注意转码
res = md5.hexdigest()
print("md5加密结果:",res,len(res))
