import json_lines
import argparse

def dataShow():
    lst =[]
    with open('tb_scr.jl', 'rb') as f:
        # lst = json_lines.reader(f)
        for item in json_lines.reader(f):
            lst.append(item)
            # print(item)
    #print(lst)
    # lst2= sorted(lst, key=lambda x : x["pointNum"],reverse=True)
    lst.sort(key=lambda x : int(x["pointNum"]),reverse=True)
    lst2 = lst
    for i in range(20):
        print(lst2[i]["title"],',',lst2[i]["pointNum"])
def main():
    dataShow()
if __name__ == "__main__":
    main()

