from kivy.uix.boxlayout import BoxLayout

class Main(BoxLayout):

    def __init__(self, *args,**arg):
        super(Main, self).__init__(*args,**arg)
        self.id = 'Main'
        # self.response = {}
        # for i in range(20):
        #     t = threading.Thread(target=self.parse,name='thread#{}'.format(i),args=(i,))
        #     t.start()
        #     t.join()
        # with open('file.txt','w',encoding='utf-8') as f:
        #     for a in self.response:
        #         for item in self.response[a]['data']['data']:
        #             item['worker_name'] = item_name = item['worker_name'].split('x')
        #             if((len(item_name)) >= 2):
        #                 f.write('F:{};N:{};S:{}\n'.format(item_name[0],item_name[1],item['status']))
        # self.response = 0
    def parse(self,i):
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
