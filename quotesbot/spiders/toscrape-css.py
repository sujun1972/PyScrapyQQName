# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'http://www.oicq88.com/shanggan/1.htm',
    ]

    def parse(self, response):
        namelist = []
        for quote in response.css("ul.list li"):
            namelist.append(quote.css("p *::text").extract_first())
            yield {
                'text': quote.css("p *::text").extract_first(),
            }

        next_page_url = response.css(".page a.next::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

