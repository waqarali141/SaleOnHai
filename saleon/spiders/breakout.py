# coding: utf-8

__author__ = 'waqarali'


import scrapy, copy

class BreakOutSpider(scrapy.Spider):
    name = 'breakout'
    base_url = 'http://www.breakout.com.pk/'
    category_test = False
    product_test = False

    def start_requests(self):
        yield scrapy.Request (url = '',
                              callback=self.parse_home_page,
                              meta = {'categories': ['test']}
                        )

        yield scrapy.Request(self.base_url, self.parse_home_page)

    def parse_home_page(self, response):
        sel = scrapy.Selector(response)
        level1_cats = sel.css('.top-menu:not(.mobile) > li:not(.lk)')

        for level1 in level1_cats:
            label1 = level1.xpath('./a/text()').extract()[0].strip()
            href1 = level1.xpath('./a/@href').extract()[0].strip()

            level2_cats = level1.css('.sublist>li')

            for level2 in level1_cats:
                label2 = level2.xpath('./a/text()').extract()[0].strip()
                href2 = level2.xpath('./a/text()').extract()[0].strip()

                meta = dict()
                meta['categories'] = [label1, label2]
                yield scrapy.Request(response.urljoin(href2), self.parse_products, meta=meta)

    def parse_products(self, response):
        sel = scrapy.Selector(response)

        products = sel.css('.product-item')

        for product in products:
            p_url = product.css('a[title]').xpath('@href').extract()[0]




            yield scrapy.Request()


