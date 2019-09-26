import os,sys
import json

import json_lines
import json



def jsonlineWrite(pfn,lst,enc="utf-8",**entries):
    with open( pfn,'w',encoding=enc) as fp:
        for item in lst:
            fp.write(json.dumps(item,**entries)+'\n')

def jsonlineShow(pfn,enc="utf-8"):
    lst =[]
    with open(pfn, 'r',encoding=enc) as f:
        for item in json_lines.reader(f):
            lst.append(item)
    return lst

import openpyxl
import json

def dictList2xls(lst,pfn):
    wb = openpyxl.Workbook()
    sheet = wb.get_active_sheet()
    keys = list(lst[0].keys())
    keys.sort()     
    sheet.append( keys)
    for d in lst:
        # sheet.append(d)
        sheet.append( [d[key]  for key  in keys] )
    wb.save(pfn)
def main():
    pfn = 'scr_jingdong3.jl'
    lst = jsonlineShow(pfn)
    pfn2 = 'scr_ingdong3.jl'
    pfn4 = 'scr_ingdong3.xls'
    print(lst)
    # jsonlineWrite(pfn2,lst[0:2],ensure_ascii=False)
    dictList2xls( lst,pfn4)
if __name__=='__main__':
    main()