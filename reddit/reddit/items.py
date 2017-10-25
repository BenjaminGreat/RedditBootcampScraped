# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedditItem(scrapy.Item):
    comments = scrapy.Field()
    #comment2 = scrapy.Field()
    #comment3 = scrapy.Field()
    #upvotes = scrapy.Field()
    #datePosted = scrapy.Field()



