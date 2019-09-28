def dictList2xls(lst,pfn):
    import openpyxl
    wb = openpyxl.Workbook()
    sheet = wb.get_active_sheet()
    keys = list(lst[0].keys())
    keys.sort()     
    sheet.append( keys)
    for d in lst:
        # sheet.append(d)
        sheet.append( [d[key]  for key  in keys] )
    wb.save(pfn)