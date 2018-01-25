# -*- coding: utf-8 -*-
import scrapy
import time
from ..items import AvitosItem




class AvitosParseSpider(scrapy.Spider):
    name = 'avitos'
    allowed_domains = ['avito.ru']
    start_urls = ['https://www.avito.ru/kazan/tovary_dlya_kompyutera/komplektuyuschie/videokarty']
    http_prefix = "https://www.avito.ru"

    def clear_list(self,lists):
        result=[]
        for l in lists:
            result.append(l.strip())
        return result

    def clear_price(self,str):
        result=str.strip("руб. ")        
        return result


    def parse(self, response):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse_page)
        pages = response.css('.clearfix a[class="pagination-page"]::attr(href)').extract()                
        for num_page in pages:
            time.sleep(5)
            yield scrapy.Request(url=self.http_prefix+num_page, callback=self.parse_page) 
        
            
    def parse_page(self, response):
        names = response.css('.item-description-title-link::text').extract()
        links = response.css('.item-description-title-link::attr(href)').extract()
        dirty_prices = response.css('.about::text')
        prices = []
        for price in dirty_prices:
            p = price.extract() 
            if p is not None:
                prices.append(p) 
            else:
                prices.append("") 
            
            """
            if len(p)>1:
                prices.append('-1')  # цена не указана
            else:
            """
            
        item = AvitosItem()
        for i in range(0,len(names)):
            item['name'] = names[i].strip()
            item['price'] = self.clear_price(prices[i].strip()).split() # "".join(self.clear_price(prices[i].strip()).split()) # сделать очистку от букв, знаков препинания, пробелы
            item['link'] = self.http_prefix + links[i]
            yield item

