# Scrapy连接到各类数据库(SQLite,Mysql,Mongodb,Redis)

[![单钒凇](https://pic1.zhimg.com/v2-534dfa2a0b1a803710fca6a122d062dc_xs.jpg)](https://www.zhihu.com/people/sfs1100)

[单钒凇](https://www.zhihu.com/people/sfs1100)

大数据人工智能机器学习数据分析Python开发爱好者



11 人赞同了该文章

这次我给大家讲讲如何使用scrapy连接到(SQLite,Mysql,Mongodb,Redis)数据库，并把爬取的数据存储到相应的数据库中。

一、SQLite

1.修改pipelines.py文件加入如下代码

```text
# 爬取到的数据写入到SQLite数据库
import sqlite3

class SQLitePipeline(object):

    #打开数据库
    def open_spider(self, spider):
        db_name = spider.settings.get('SQLITE_DB_NAME', 'scrapy.db')

        self.db_conn = sqlite3.connect(db_name)
        self.db_cur = self.db_conn.cursor()

    #关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    #对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
        values = (
            item['upc'],
            item['name'],
            item['price'],
            item['review_rating'],
            item['review_num'],
            item['stock'],
        )

        sql = 'INSERT INTO books VALUES(?,?,?,?,?,?)'
        self.db_cur.execute(sql, values)
```



2.修改settings.py文件，加入如下代码

```text
# sqlite 配置
SQLITE_DB_NAME = 'scrapy.db'
```

在settings启动管道文件

```text
ITEM_PIPELINES = {
   'toscrape_book.pipelines.SQLitePipeline': 400,
}
```



二、mysql

1.修改pipelines.py文件加入如下代码

```text
# 爬取到的数据写入到MySQL数据库
import pymysql
class MySQLPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME','scrapy_db')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', '123456')

        self.db_conn =pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
        values = (
            item['upc'],
            item['name'],
            item['price'],
            item['review_rating'],
            item['review_num'],
            item['stock'],
        )

        sql = 'INSERT INTO books VALUES(%s,%s,%s,%s,%s,%s)'
        self.db_cur.execute(sql, values)
```

2.修改settings.py文件，加入如下代码

```text
# mysql 配置
MYSQL_DB_NAME = 'scrapy_db'
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
```

在settings启动管道文件

```text
ITEM_PIPELINES = {
   'toscrape_book.pipelines.MySQLPipeline': 401,
}
```

三、mongodb

1.修改pipelines.py文件加入如下代码

```text
# 爬取到的数据写入到Mongodb数据库
from pymongo import MongoClient
from scrapy import Item

class MongoDBPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        db_uri = spider.settings.get('MONGODB_URI', 'mongodb://localhost:27017')
        db_name = spider.settings.get('MONOGDB_DB_NAME', 'scrapy_db')

        self.db_client = MongoClient(db_uri)
        self.db = self.db_client[db_name]

    # 关闭数据库
    def close_spider(self, spider):
        self.db_client.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    # 插入数据
    def insert_db(self, item):
        if isinstance(item, Item):
            item = dict(item)
        self.db.books.insert(item)
```

2.修改settings.py文件，加入如下代码

```text
# mongodb 配置
MONGODB_URI = 'mongodb://127.0.0.1:27017'
MONGODB_DB_NAME = 'scrapy_db'
```

在settings启动管道文件

```text
ITEM_PIPELINES = {
   'toscrape_book.pipelines.MongoDBPipeline': 403,
}
```

四、redis

1.修改pipelines.py文件加入如下代码

```text
# 爬取到的数据写入到redis数据库
import redis
from scrapy import Item

class RedisPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        db_host = spider.settings.get('REDIS_HOST', 'localhost')
        db_port = spider.settings.get('REDIS_PORT', 6379)
        db_index = spider.settings.get('REDIS_DB_INDEX', 0)

        self.db_conn = redis.StrictRedis(host=db_host, port=db_port, db=db_index)
        self.item_i = 0

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.connection_pool.disconnect()

    # 处理数据
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    # 插入数据
    def insert_db(self, item):
        if isinstance(item, Item):
            item = dict(item)

        self.item_i += 1
        self.db_conn.hmset('book:{}'.format(self.item_i), item)
```

2.修改settings.py文件，加入如下代码

```text
# redis 配置
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB_INDEX = 0
```

在settings启动管道文件

```text
ITEM_PIPELINES = {
   'toscrape_book.pipelines.RedisPipeline': 404,
}
```



scrapy 连接各数据的设置并不复杂，首先在pipelines文件中建立管道，建立个数据的连接，然后处理数据，关闭连接。接下来我们在settings文件中定义各类数据库的基本配置，然后在item_pipelines中启动相应的管道