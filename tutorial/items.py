# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    address = scrapy.Field()
    formattime = scrapy.Field()
    money = scrapy.Field()
    exper = scrapy.Field()
    edu = scrapy.Field()
    company = scrapy.Field()
    companylink = scrapy.Field()
    industry = scrapy.Field()
    attract = scrapy.Field()
    tags = scrapy.Field()
    companylogo = scrapy.Field()
    pass
