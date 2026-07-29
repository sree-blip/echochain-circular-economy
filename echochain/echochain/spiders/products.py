import scrapy
import random

class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = ["https://example.com"]

    def parse(self, response):

        categories = [
            "Mobile",
            "Laptop",
            "Furniture",
            "Electronics",
            "Accessories"
        ]

        for i in range(1, 61):

            yield {
                "product_id": i,
                "product_name": f"Product_{i}",
                "category": random.choice(categories),
                "price": random.randint(1000, 50000)
            }