from scrapy import Selector

body = '<html><head><title>Hello world</title></head><body></body></html>'
selector = Selector(text=body)
title = selector.xpath('//title/text()').extract_first()
print(title)
