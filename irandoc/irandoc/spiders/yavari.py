import scrapy


class YavariSpider(scrapy.Spider):
    name = 'yavari'
    allowed_domains = ['irandoc.ac.ir']
    start_urls = ['https://ganj.irandoc.ac.ir/api/v1/search/advance?basicscope_1=1&basicscope_2=1&basicscope_3=1&fulltext_status=1&keywords_1=الهام+یاوری&keywords_2=&keywords_3=&limitation=&operator_1=1&operator_2=1&results_per_page=2&sort_by=1&year_from=0&year_to=1400']

    def parse(self, response):
        SET_SELECTOR=".box search_result ng-scope"
        print("haha ", response.css(SET_SELECTOR))
        for selectorcount in response.css(SET_SELECTOR):
            print("hahaha ",selectorcount.css('span.search_title::text').get())
            yield {
                'search_title':selectorcount.css('span.search_title::text').get()
            }
        pass
