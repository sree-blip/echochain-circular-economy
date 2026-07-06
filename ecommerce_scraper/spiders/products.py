import scrapy

class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        titles = response.css("h3 a::attr(title)").getall()

        for title in titles:
            yield {
                "title": title
            }