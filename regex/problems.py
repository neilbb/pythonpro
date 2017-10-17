
#specify encoding just in case
#open("nameoffile.txt",encoding="utf-8")

import re

if __name__ == '__main__':
    f = open("names.txt" ,encoding='utf-8',mode='r')
    #for i in f:
    #   print(i)

    a = f.read()

    f.close()




   # print(re.match(r"Lore",a))
   # print(50*'*')
   # print(re.search(r"ore",a))
    #print(80*'*')

    #print(re.findall(r'\(?\d+\)?-?\s?\d+-\d+',a))
    print(re.findall(r'tree+',a,re.IGNORECASE))

    #\d any number
    #\w any character

    #print(a)





