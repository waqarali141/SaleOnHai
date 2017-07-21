# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class SaleonItem(Item):
    # define the fields for your item here like:

    base_sku = Field(type='str')
    identifier = Field(type='str')

    title = Field(type='str')

    color_name = Field(type='str')
    color_code = Field(type='str')

    brand = Field(type='str')
    categories = Field(type='list')

    image_urls = Field(type='list')
    url = Field(type='str')

    orginal_price = Field(type='str')
    sale_price = Field(type='str')
    full_price = Field(type='str')

    size_infos = Field(type='list')

    isonsale = Field()
    isnew = Field()
    available = Field()

    pass
