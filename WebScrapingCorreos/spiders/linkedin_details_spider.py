import scrapy
import json

class LinkedinDetailsSpider(scrapy.Spider):
    name = 'linkedin_details'
    start_urls = []

    def start_requests(self):
        with open('output.json', 'r') as file:
            urls = json.load(file)
            for url in urls:
                yield scrapy.Request(url=url['url-pagina'], callback=self.parse_details)

    def parse_details(self, response):
        yield {
            'Name': response.xpath('//some/xpath/for/name').get(),
            'Is Business': response.xpath('//some/xpath/for/business').get(),
            'Email': response.xpath('//some/xpath/for/email').get(),
            'Address': response.xpath('//some/xpath/for/address').get(),
            'Phone': response.xpath('//some/xpath/for/phone').get(),
            'Extra': response.xpath('//some/xpath/for/extra').get()
        }
