import scrapy, json
from datetime import datetime


class IrandocSpider(scrapy.Spider):
    name = 'irandoc'
    start_urls = [
        'https://ganj.irandoc.ac.ir/api/v1/search/main?basicscope=5&fulltext_status=1&keywords=%D8%B5%D8%A7%D8%AF%D9%82+%D8%AF%D8%B1%DB%8C+%D9%86%D9%88%DA%AF%D9%88%D8%B1%D8%A7%D9%86%DB%8C&results_per_page=4&sort_by=1&year_from=0&year_to=1400&page=1'
    ]
    tags_base_url = 'https://ganj.irandoc.ac.ir/api/v1/articles/{uuid}/show_tags'
    base_url= 'https://ganj.irandoc.ac.ir/api/v1/search/main?basicscope=5&fulltext_status=1&keywords={keyword}&results_per_page=4&sort_by=1&year_from=0&year_to=1400'
    started_time=0
    def __init__(self):
        self.started_time=datetime.now()
        super(IrandocSpider, self).__init__()

    def parse(self, response):
        print('phase 1')
        content = json.loads(response.text)
        print('len ',content['results'])
        for link in content['results']:
            item = {
                'title':link['title'],
                'tags': [],
            }
            # yield {'uuid':link['uuid']}
            yield scrapy.Request(self.tags_base_url.format(uuid=link['uuid']),
                                 self.tags_parse, meta={'item': item})

        print("PAGINGGGGGGGGGGGG")
        total_pages=content['total_pages']
        if(total_pages >= 2):
            print('total_paes',total_pages)
            for i in range(2,total_pages+1):
                yield scrapy.Request(f'{self.base_url.format(keyword="صادق دری نوگورانی")}&page={i}',callback=self.parse)


    def tags_parse(self, response):
        print('phase 2')
        if (len(response.text) > 0):
            cnt = json.loads(response.text)
            tags=[]
            for item in cnt['tags']:
                tags.append({
                    'title_en':item['title_en'],
                    'title_fa':item['title_fa'],
                })
            response.request.meta['item']['tags']=tags
        return response.request.meta['item']


    def __del__(self):
        diff=datetime.now()-self.started_time
        print('total seconds  ',diff.total_seconds())
