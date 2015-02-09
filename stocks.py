#stocks.py
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from nasdaq.items import NasdaqItem

#instantiates the mail sender
from scrapy.mail import MailSender
mailer = MailSender()

#nasdaq class
class nasdaq(CrawlSpider):
    name = "nasdaq"
    allowed_domains = ["nasdaq.com"]
    start_urls = ["http://nasdaq.com/symbol/intc/after-hours"]


#Extracts a page of trade detial follows rule to exact webpage address    
    rules = [
    Rule(SgmlLinkExtractor(allow=("http://nasdaq.com/symbol/intc/after-hours")), follow=True),
    Rule(SgmlLinkExtractor(allow=()), callback='parse_item')
]
   

#Parse function for extracting the stock ticker name,current price,date stamp.
# Where stn=stock ticker name, cp=current price, dstmp=date stamp
#xpath to get exact data wanted stn,cp,dstmp
    def parse_item(self,response):
    	#log message to show scrapy is extracting
        self.log('Hi! am going to start extractinging now')
        sel=Selector(response)
        item=NasdaqItem()
        #Xpath for stock tinker name
        item['stn'] = sel.xpath('//span/a[@class="qn_ontab"]/text()').extract()
        #Xpath for current price
        item['cp'] = sel.xpath('//div[@id="qwidget_lastsale"]/text()').extract()
        #Xpath for date stamp
        item['dstmp'] = sel.xpath('//span[@id="qwidget_markettime"]/text()').extract()
        return item
		
#Function to send email	(did not work might have to read more on the process)
	mailer.send(to=["kofdossou@gmail.com"], subject="Some subject", body="Some body", cc=["kdossou@csu.edu"])
