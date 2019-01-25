import scrapy
from tutorial.items import TutorialItem

class LagouSpider(scrapy.Spider):
    name = "lagou"

    def start_requests(self):
        urls = [
            'https://www.lagou.com/zhaopin/Java/?labelWords=label',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        itemlist = response.css(".con_list_item")

        if itemlist is not None:

            for item in itemlist:
                required = item.css(".li_b_l::text").extract()[2].strip().split('/')
                exper = required[0].strip()
                edu = required[1].strip()
                totorial_item = TutorialItem()

                totorial_item['title'] = item.css("a h3::text").extract_first()
                totorial_item['href'] = item.css("a::attr(href)").extract_first()
                totorial_item['address'] = item.css("a em::text").extract_first()
                totorial_item['formattime'] = item.css(".format-time::text").extract_first()
                totorial_item['money'] = item.css(".money::text").extract_first()
                totorial_item['exper'] = exper
                totorial_item['edu'] = edu
                totorial_item['company'] = item.css(".company_name a::text").extract_first()
                totorial_item['companylink'] = item.css(".company_name a::attr(href)").extract_first()
                totorial_item['industry'] = item.css(".industry::text").extract_first().strip().split('/')
                totorial_item['attract'] = item.css(".li_b_r::text").extract_first()
                totorial_item['tags'] = item.css(".list_item_bot span::text").extract()
                totorial_item['companylogo'] = item.css(".com_logo img::attr(src)").extract_first()
                yield totorial_item
                # yield {
                #     'title':item.css("a h3::text").extract_first(),
                #     'href':item.css("a::attr(href)").extract_first(),
                #     'address':item.css("a em::text").extract_first(),
                #     'formattime':item.css(".format-time::text").extract_first(),
                #     'money':item.css(".money::text").extract_first(),
                #     'exper':exper,
                #     'edu':edu,
                #     'company':item.css(".company_name a::text").extract_first(),
                #     'companylink':item.css(".company_name a::attr(href)").extract_first(),
                #     'industry':item.css(".industry::text").extract_first().strip().split('/'),
                #     'attract':item.css(".li_b_r::text").extract_first(),
                #     'tags':item.css(".list_item_bot span::text").extract(),
                #     'companylogo':item.css(".com_logo img::attr(src)").extract_first(),
                # }

            next_page_url = response.css(".pager_container a")[-1].css("::attr(href)").extract_first()
            if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url))
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)