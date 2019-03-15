# -*- coding: utf-8 -*-
import scrapy

#demo.py简化版
#class DemoSpider(scrapy.Spider):
#    name = 'demo'
#    #allowed_domains = ['python123.io']
#    start_urls = ['http://python123.io/ws/demo.html']

#    def parse(self, response):
#	    fname = response.url.split('/')[-1]
#	    with open(fname, 'wb') as f:
#	        f.write(response.body)
#	    self.log('Saved file %s.' %name)
#	    pass

#demo.py完整版
class DemoSpider(scrapy.Spider):
	name = "demo"
	def start_requests(self):
		urls = [
				'http://python123.io/ws/demo.html'
				]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)
	
	def parse(self, response):
		fname = response.url.split('/')[-1]
		with open (fname, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s.' %fname)
