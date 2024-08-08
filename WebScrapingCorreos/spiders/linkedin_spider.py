# import scrapy # UNA paginas  

# class LinkedinSpider(scrapy.Spider):
#     name = 'linkedin'
#     start_urls = [
#         'https://www.bing.com/search?q=%22Pedro-argentinaa%22%40gmail.com%20linkedin'
#     ]

#     def parse(self, response):
#         for result in response.xpath('//li[@class="b_algo"]'):
#             yield {
#                 'Name': result.xpath('.//h2/a/text()').get(),
#                 'Is Business': None,  # Custom logic needed
#                 'Email': result.xpath('.//h2/a/@href').get(),
#                 'Address': None,  # Custom logic needed
#                 'Phone': None,  # Custom logic needed
#                 'Extra': result.xpath('.//p/text()').get()
#             }

#         next_page = response.xpath('//a[@title="Next page"]/@href').get()
#         if next_page:
#             yield scrapy.Request(url=next_page, callback=self.parse)
 
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
            'Profile Picture URL': response.xpath('//button[contains(@aria-label, "abrir la foto del perfil")]//img/@src').get(),
            'Current Company': response.xpath('//li[contains(@class, "YhCbXgtTNvusUHWUOSEztKCHzGtPJzHxs")]/button/span[contains(@class, "hoverable-link-text")]/div/text()').get(),
            'Education': response.xpath('//li[contains(@class, "YhCbXgtTNvusUHWUOSEztKCHzGtPJzHxs")]/button/span[contains(@class, "hoverable-link-text")]/div/text()').get(),
            'Location': response.xpath('//span[contains(@class, "text-body-small") and contains(@class, "t-black--light")]/text()').get(),
            'Contact Info Link': response.xpath('//a[@id="top-card-text-details-contact-info"]/@href').get(),
            'Website': response.xpath('//section[contains(@class, "pv-top-card--website")]/a/@href').get(),
        }
