# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticuloscrawlItem(scrapy.Item):
    precio_del_articulo = scrapy.Field()
    enlace_del_articulo = scrapy.Field()
    nombre_del_articulo = scrapy.Field() 
    vendedor_del_articulo = scrapy.Field()
    image_urls = scrapy.Field()
    