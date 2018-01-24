# -*- coding: utf-8 -*-
import scrapy
from ..items import AvitosItem


class AvitosParseSpider(scrapy.Spider):
    name = 'avitos'
    allowed_domains = ['avito.ru']
    start_urls = ['https://www.avito.ru/kazan/tovary_dlya_kompyutera/komplektuyuschie/videokarty']
    http_prefix = "https://www.avito.ru"

    def parse(self, response):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse_page)
        pages = response.css('.clearfix a[class="pagination-page"]::attr(href)').extract()
        """
        for num_page in pages:
            yield scrapy.Request(url=self.http_prefix+num_page, callback=self.parse_page) 
        """

    def parse_page(self, response):
        print("\nТекущая страница = ",response.url+"\n")
        #response.css('.item-description-title-link::text').extract()
        links = response.css('.item-description-title-link::attr(href)').extract()
        for link in links:
            yield scrapy.Request(url=self.http_prefix+link, callback=self.parse_tovar) 

    def parse_tovar(self, response):
        item = AvitosItem()
        name = response.css('.title-info-title-text::text').extract_first()
        item['name'] = name

        yield item


