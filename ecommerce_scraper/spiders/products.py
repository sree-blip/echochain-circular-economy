import scrapy
import time


class ProductsSpider(scrapy.Spider):

    name = "products"

    start_urls = [
        "http://127.0.0.1:5000/"
    ]

    custom_settings = {
        "ROBOTSTXT_OBEY": False,

        "FEEDS": {
            "day11_products.csv": {
                "format": "csv",
                "encoding": "utf-8",
                "overwrite": True,
            }
        },

        "CONCURRENT_REQUESTS": 64,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 32,
        "DOWNLOAD_DELAY": 0.1,
        "RETRY_ENABLED": True,
        "RETRY_TIMES": 3,
        "DOWNLOAD_TIMEOUT": 10,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_time = time.time()
        self.count = 0

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, errback=self.handle_error)

    def handle_error(self, failure):
        self.logger.error(f"Request failed: {failure.request.url} - {failure.value}")

    def parse(self, response):

        products = response.css("div.col-md-4 .card")

        for product in products:

            try:
                product_name = product.css("h5::text").get()

                if not product_name:
                    continue

                data = {}

                for p in product.css("p"):
                    text = " ".join(p.xpath(".//text()").getall())
                    text = " ".join(text.split())

                    if text.startswith("Brand:"):
                        data["brand"] = text.replace("Brand:", "").strip()

                    elif text.startswith("Category:"):
                        data["category"] = text.replace("Category:", "").strip()

                    elif text.startswith("Condition:"):
                        data["condition"] = text.replace("Condition:", "").strip()

                    elif text.startswith("Seller:"):
                        data["seller_name"] = text.replace("Seller:", "").strip()

                    elif text.startswith("Rating:"):
                        data["seller_rating"] = text.replace("Rating:", "").replace("⭐", "").strip()

                    elif text.startswith("Location:"):
                        data["location"] = text.replace("Location:", "").strip()

                self.count += 1

                yield {
                    "product_name": product_name.strip(),
                    "brand": data.get("brand", ""),
                    "category": data.get("category", ""),
                    "condition": data.get("condition", ""),
                    "seller_name": data.get("seller_name", ""),
                    "seller_rating": data.get("seller_rating", ""),
                    "location": data.get("location", ""),
                    "resale_price": product.css(
                        ".price::text"
                    ).get(default="").strip(),
                    "product_url": product.css(
                        "a[href*='/product/']::attr(href)"
                    ).get(default="").strip(),
                    "scraped_date": time.strftime("%Y-%m-%d")
                }

            except Exception as e:
                self.logger.error(f"Error parsing product: {e}")
                continue

    def closed(self, reason):

        total_time = time.time() - self.start_time

        print("\n" + "=" * 50)
        print("DAY 11 - SCRAPER PERFORMANCE")
        print("=" * 50)

        print(f"Total Products Scraped : {self.count}")
        print(f"Total Time             : {total_time:.2f} seconds")

        if total_time > 0:
            print(
                f"Scraping Speed         : "
                f"{self.count / total_time:.2f} products/sec"
            )

        print(f"Spider Close Reason    : {reason}")
        print("=" * 50)