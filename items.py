from scrapy.item import Item, Field


class TencentItem(Item):

    name = Field()
    catalog = Field()
    workLocation = Field()
    recruitNumber = Field()
    detailLink = Field()
    publishTime = Field()
