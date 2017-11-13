# -*- coding: utf-8 -*-
#Autor: Antonio Arencibia Guerra
import scrapy
from articuloscrawl.items import ArticuloscrawlItem

class ArtcrawlSpider(scrapy.Spider):
#Nombre de spider  
    name = 'artcrawl'
# Dominios permitidos   
    allowed_domains = ['www.amazon.es']
# URLs donde comenzará la extracción de los datos. Este caso llegará hasta la pagina 5 de los resultados mostrados bajo la keyword "guitarras"
    start_urls = ['https://www.amazon.es/s/ref=sr_pg_1?rh=i%3Aaps%2Ck%3Aguitarras&page={}&keywords=guitarras&ie=UTF8&qid=1510550565'.format(i) for i in range(0,5)]
    
 
    def parse(self, response): 
#Datos a extraer de cada articulo mediante comandos xpath      
        precio = response.xpath('//span[contains(@class,"a-offscreen")]/text()').extract()
        enlace = response.xpath('//a[contains(@class,"s-access-detail-page")]/@href').extract()                     
        nombre = response.xpath('//h2[contains(@class,"s-access-title")]/text()').extract()
        vendedor = response.xpath('//div[@class="a-row a-spacing-none"]/span[@class="a-size-small a-color-secondary"][2]/text()').extract()
        image_urls = response.xpath('//a[@class="a-link-normal a-text-normal"]/img/@src').extract()
        
        l= len(nombre)


        for i in range(0,l):
            
            articulo = ArticuloscrawlItem()
            articulo ['precio_del_articulo']= precio[i]
            articulo ['enlace_del_articulo'] = enlace[i]           
            articulo ['nombre_del_articulo'] = nombre[i]           
            articulo ['vendedor_del_articulo'] = vendedor[i]
            articulo ['image_urls'] = image_urls[i]

            yield articulo