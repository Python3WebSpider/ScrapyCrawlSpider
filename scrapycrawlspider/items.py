from scrapy import Field, Item

class NewsItem(Item):
    title = Field()
    text = Field()
    datetime = Field()
    source = Field()
    url = Field()
    website = Field()