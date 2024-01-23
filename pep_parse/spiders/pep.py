import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, SPIDER_NAME, START_URLS


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        peps = response.css('a.pep::attr(href)')
        for pep_link in peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.css('h1.page-title::text').get().split()[1],
            'name': ' '.join(
                response.css('h1.page-title::text').get().split()[3:]
            ),
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
