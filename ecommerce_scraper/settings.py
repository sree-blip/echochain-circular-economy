BOT_NAME = "ecommerce_scraper"

SPIDER_MODULES = ["ecommerce_scraper.spiders"]
NEWSPIDER_MODULE = "ecommerce_scraper.spiders"

# Day 11 - Performance Optimization

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 16
DOWNLOAD_DELAY = 0

COOKIES_ENABLED = False

FEED_EXPORT_ENCODING = "utf-8"