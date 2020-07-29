__author__ = 'Naoi'

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Pregunta(Item):
    pregunta = Field()
    id = Field()

class StackOverflowSpider(Spider):
    name = "MiPrimerSpider"
    start_urls = ['http://www.gestpymeweb.cl/gestdocu/PAGE_Login/SBAAABYnLqtkZFZFUkp4bW1kAwA']
    def parse(self, response):
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="A4_1_0"]/div')

        #Iterar sobre todas las preguntas
        for i, elem in enumerate(preguntas):
            item = ItemLoader(Pregunta(), elem)
            item.add_xpath('pregunta', './/div/text()')
            item.add_value('id', i)

            yield item.load_item()
