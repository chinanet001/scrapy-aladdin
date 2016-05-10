#-*- coding: UTF-8 -*-
import json

data = []
with open('aladdin/aladdin.json') as f:
    for line in f:
        data.append(json.loads(line))

#print json.dumps(data, ensure_ascii=False)

str = "\r\n"
for item in data:
    #print json.dumps(item)
    str = str + "insert into tencent(name,phone) values "
    str = str + "('%s','%s');\r\n" % (item['name'],item['phone'])

import codecs
file_object = codecs.open('aladdin.sql', 'w' ,"utf-8")
file_object.write(str)
file_object.close()
print "success"

