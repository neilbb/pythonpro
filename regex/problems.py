
#specify encoding just in case
#open("nameoffile.txt",encoding="utf-8")

import re

if __name__ == '__main__':
    f = open("sample.txt" ,encoding='utf-8',mode='r')
    #for i in f:
    #   print(i)

    a = f.read()



    print(re.match(r"Lore",a))
    print(50*'*')
    print(re.search(r"ore",a))



    #print(a)
    f.close()




