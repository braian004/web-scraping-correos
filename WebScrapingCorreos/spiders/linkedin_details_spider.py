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
            'Name': response.xpath('//h1[contains(@class, "text-heading-xlarge")]/text()').get(),
            'Title': response.xpath('//div[contains(@class, "text-body-medium")]/text()').get(),
            'Profile Picture URL': response.xpath('//button[contains(@aria-label, "foto del perfil")]//img/@src').get(),
            'Current Company': response.xpath('//li[contains(@class, "YhCbXgtTNvusUHWUOSEztKCHzGtPJzHxs")]//span[contains(@class, "hoverable-link-text")]//div/text()').get(),
            'Education': response.xpath('//li[contains(@class, "YhCbXgtTNvusUHWUOSEztKCHzGtPJzHxs")]//span[contains(@class, "hoverable-link-text")]//div/text()').get(),
            'Location': response.xpath('//span[contains(@class, "text-body-small") and contains(@class, "t-black--light")]/text()').get(),
            'Contact Info Link': response.xpath('//a[@id="top-card-text-details-contact-info"]/@href').get(),
            'Website': response.xpath('//section[contains(@class, "pv-top-card--website")]//a/@href').get(),
        }
