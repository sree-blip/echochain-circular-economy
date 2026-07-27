import scrapy

class ProductSpider(scrapy.Spider):
    name = "products"
    start_urls = [
        "https://example.com/products"
    ]

    def parse(self, response):
        products = response.css("div.product")

        for product in products:
            name = product.css("h2::text").get()
            price = product.css(".price::text").get()

            if name and price:
                yield {
                    "product_name": name.strip(),
                    "price": price.strip()
                }