def dict2cmdline(dct):
    lst =[]
    for d in dct:
        if not d.startswith('_') and dct[d] is not None :
            b = dct[d]
            if isinstance( b,dict):
                for k in b:
                    print( d,k,b[k])
                    lst.extend( ['--%s'% d  ,  k+'='+ str(b[k])  ])
            elif isinstance(b,list):
                for s in b:
                    lst.extend( ['--%s'% d  ,  s ])
            else:
                lst.extend( ['--%s'% d  , b ])            
    return lst

def removeDirtyChar(s):
    move = dict.fromkeys((ord(c) for c in u"\xa0\n\t\u3000"))
    return s.translate(move)
def main():
    inputstring = u'\n               Door:\xa0Novum    \t'
    move = dict.fromkeys((ord(c) for c in u"\xa0\n\t"))
    output = inputstring.translate(move)
    print(output)
if __name__ == "__main__":
    pass