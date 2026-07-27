import scrapy

class ProductsSpider(scrapy.Spider):
    name = "products"
    
    # Pagination loop (1 to 5 pages)
    def start_requests(self):
        for page in range(1, 5):
            url = f"https://echochain-e-commerce-ca8d.bolt.host/?page={page}"
            yield scrapy.Request(url=url, callback=self.parse, meta={'page_number': page})

    def parse(self, response):
        page_num = response.meta.get('page_number', 1)
        products = response.css("div.product, div.card, article")
        
        for prod in products:
            yield {
                "product_name": prod.css("h1::text, h2::text, h3::text, .title::text").get(),
                "resale_price": prod.css("span.price::text, .price::text").get(),
                "page_number": page_num,
                "source_url": response.url
            }