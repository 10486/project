# -*- coding: utf-8 -*-

import threading
import requests
import json
class Parser(object):
    def __init__(self,file='file.txt'):
        self.response = {}
        self.file = file
    def loadinfo(self):
        for i in range(20):
            t = threading.Thread(target=self.__parse,name='thread#{}'.format(i),args=(i,))
            t.start()
            t.join()
        self.info = {x+1 : {'ACTIVE':[],'INACTIVE':[]} for x in range(26)}

        for a in self.response:
            for item in self.response[a]['data']['data']:
                item['worker_name'] = item_name = item['worker_name'].split('x')
                if((len(item_name)) >= 2):
                    self.info[int(item_name[0])][item['status']].append(item_name[1])
        with open(self.file,'w',encoding='utf-8') as f:
            f.write(json.dumps(self.info))
        del self.info

    def __parse(self,i):
        url = '\
https://eu-pool.api.btc.com/v1/worker/?group=0\
&page={}\
&page_size=50\
&status=active\
&order_by=worker_name\
&asc=1&filter=\
&access_key=r_0CNsYyaUYTevJ\
&puid=207067\
&lang=en'.format(i+1)
        dict = json.loads(requests.get(url).content)
        self.response[str(i)] = dict

    def clear(self):
        self.response = {}
