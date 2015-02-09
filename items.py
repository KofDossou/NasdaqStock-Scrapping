items.py
=========
from scrapy.item import Item, Field

class NasdaqItem(Item):
    # define the  specific field items we want from webiste
    stn = Field()
    cp = Field()
    dstmp = Field()
