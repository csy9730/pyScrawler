# -*- coding: utf-8 -*-
'''
Created on 2018年6月20日

@author: zww
'''
from selenium import webdriver
import pymysql
import time
import os

import random
from urllib import request


class DouBanPics:
    def __init__(self, isbnlist):
        path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.wb = webdriver.Chrome(executable_path=path)
        # 根据isbn来抓取
        self.isbn_list = isbnlist
        # 字典存放isbn对应的图片地址
        self.pics_url = {}

# 爬取isbn对应的图片地址
    def getPicsUrl(self):
        for isbn in self.isbn_list:
 　　　 # 每抓一个休眠一个随机时间，免得被封了IP

　　　　time.sleep(round(random.uniform(1, 4), 2))


            # 根据isbn来查询书籍
            self.wb.get(
                'https://book.douban.com/subject_search?search_text=%s&cat=1001' % isbn)
            # 获取大图
            self.wb.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/a/img').click()
            # 获取图片地址
            self.wb.find_element_by_xpath('//*[@id="mainpic"]/a/img').click()
            # 当前页面的url就是图片地址
            img_url = self.wb.current_url
            # 通过字典存放
            self.pics_url[isbn] = img_url

# 只把图片的地址存到数据库中
    def savePicsUrls(self):
        try:
            # 连接数据库的信息也可以通过配置来取，这里就直接写死了
            self.db = DataBaseHandle(
                'ip', 3306, 'root', '密码', 数据库名')
            for key in self.pics_url.keys():
                sql = '''insert into doubanpics(isbn,imgurl) values("%s","%s")''' % (
                    key, self.pics_url[key])
                self.db.insert_sql(sql)
        except Exception as e:
            print(e)
        finally:
            self.db.close()

# 把图片下载到本地
    def savePics(self, path='D:\\doubanPics'):
        # 目录不存在，就新建一个
        if not os.path.exists(path):
            os.makedirs(path)

        for key in self.pics_url.keys():
            # 这里要取图片地址的最后一个，以便之后获取图片的格式，保存的时候就按照本来的格式保存
            lastname = self.pics_url[key].split('/')
            prefix, Suffix = lastname[-1].split('.')
            # 组装图片的绝对路径，用isbn来命名
            pic_path = ''.join([path, '\\', str(key), '.', Suffix])
            req = request.Request(self.pics_url[key], headers={
                                  'User-Agent':  r'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'})
            data = request.urlopen(req, timeout=30).read()
            f = open(pic_path, 'wb')
            f.write(data)
            f.close()


# 数据库操作类
class DataBaseHandle:
    def __init__(self, ip, port, user, passwd, db_name):
        self.con = pymysql.connect(
            host=ip, port=port, user=user, passwd=passwd, db=db_name, charset='utf8')
        self.cursor = self.con.cursor()

    # 执行查询SQL
    def select_sql(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
#         row = self.cursor.fetchone()
        return result

    # 执行插入SQL
    def insert_sql(self, sql):
        self.cursor.execute(sql)
        self.con.commit()

    # 执行更新SQL
    def update_sql(self, sql):
        self.cursor.execute(sql)
        self.con.commit()

    # 执行关闭连接
    def close(self):
        self.cursor.close()
        self.con.close()
# isbn放在excel里面，从excel中读取isbn
class ExcelHandle:
    def __init__(self, excel_path):
        self.excel_obj = xlrd.open_workbook(excel_path)
        self.sheet = self.excel_obj.sheet_by_index(0)

    def getIsbnList(self):
        rows = self.sheet.nrows
        isbn_list = []
        for i in range(1, rows):
            isbn = self.sheet.cell_value(i, 0)
            isbn_list.append(isbn)
        return isbn_list



def main():
    excel_obj = ExcelHandle('isbnList.xlsx')
    isbnlist = excel_obj.getIsbnList()
    dbpics = DouBanPics(isbnlist)
    # 获取图片地址
    dbpics.getPicsUrl()
    # 只存url地址
    dbpics.savePicsUrls()
    # 下载图片到本地
    dbpics.savePics()


if __name__ == '__main__':
    main()