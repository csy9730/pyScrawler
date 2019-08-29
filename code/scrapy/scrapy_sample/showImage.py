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

def main():
    pfn = 'scr_mm131.jl'
    lst = dataShow(pfn )

    lst2= sorted(lst, key=lambda x : x["referer"],reverse=True)
    # lst.sort(key=lambda x : int(x["referer"]),reverse=True)
    for i in range(20):
        print(lst2[i]["title"],',',lst2[i]["referer"])
    # print(lst2)
if __name__ == "__main__":
    main()