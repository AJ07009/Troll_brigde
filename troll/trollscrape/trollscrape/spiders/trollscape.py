import scrapy


class TrollscapeSpider(scrapy.Spider):
    name = "trollscape"
    allowed_domains = ["tcgplayer.com"]
    start_urls = ["https://tcgplayer.com"]

    def parse(self, response):
        pass
