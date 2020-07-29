from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Habitacion(Item):
  titulo = Field()
  huespedes = Field()
  caracteristicas = Field()



class AirbnbCrawlerVertical(CrawlSpider):
  name = "CrawlerVertical"
  custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
  }
  start_urls = ["http://www.gestpymeweb.cl/gestdocu/PAGE_Login/SBAAAFXlRatkZFZFUkp4bW1kAwA"]

  allowed_domains = ["http://www.gestpymeweb.cl/"]
  download_delay = 1
  rules = (
    Rule(LinkExtractor(allow=r'/rooms'), callback = 'parse_items'),
  )

  def procesarHuespedes(self, texto):
    if (texto and len(texto) > 1):
      texto_dividido = texto.split(' ')
      return texto_dividido[0]
    return '0'


  def parse_items(self, response):
    sel = Selector(response)
    item = ItemLoader(Habitacion(), sel)
    item.add_xpath('Rut', '//div/text()')
    item.add_xpath('Nombre', '//div/text()')

    yield item.load_item()
