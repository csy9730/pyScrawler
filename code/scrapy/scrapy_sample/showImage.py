import json_lines
import argparse


def dataShow(pfn):
    lst =[]
    with open(pfn, 'rb') as f:
        # lst = json_lines.reader(f)
        for item in json_lines.reader(f):
            lst.append(item)
            #print(item)
    return lst

def imgMove(lst,dirNew='images/'):
    ls = []
    for dct in lst:
        images = dct["images"]
        import os,sys
        pth =  dirNew+dct["img_folder"]
        os.mkdir(pth)
        for img in images:
            url = img["url"]
            filenameOld = 'images/'+img["path"]
            filenameNew = pth+'/'+url.split('/')[-1]
            print(filenameOld,filenameNew)#
            os.rename(filenameOld,filenameNew)#重命
            ls.append( filenameNew )
    return ls
def eSqlite():
    import sqlite3
    db_name ='scr_image.db'
    db_conn = sqlite3.connect(db_name)
    sql = "select ID,REFERER, image_url , path,title from images"
    sel = db_conn.execute(sql)
    for s in sel:
        print(s[0],s[1],s[2],s[3].decode('utf-8'),s[4].decode('utf-8'))
    db_conn.close()


def main():
    eSqlite()
    return
    pfn = 'scr'
    pfn = 'scr_mm131.jl'
    lst = dataShow(pfn )
    img2 = imgMove(lst)
    return 
    lst2= sorted(lst, key=lambda x : x["referer"],reverse=True)
    # lst.sort(key=lambda x : int(x["referer"]),reverse=True)
    for i in range(20):
        print(lst2[i]["title"],',',lst2[i]["referer"])
    # print(lst2)
if __name__ == "__main__":
    main()