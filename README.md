koffi-quick-scraper
===================
 This a nasdaq.com scrapper.It scrapes intc data specfically:
######stock ticker name(stn)
######current price(cp)
######datetime stamps(dstmp)
 
#Tools used: 
######Scrapy framework
######Python
######Notepad++
######Website visited by scrapy: http://www.nasdaq.com/symbol/intc/after-hours
######Xpath
#Procedure
To run this project one will need Scrapy framework downloaded on their C: drive in conjunction with python
######Copy and paste data in items.py
######Create a .py file (in my case i used stocks.py(copy code from stocks.py to run) as file name)
######Navigate in Scrapy to directory where your scrapy project is located(eg C:\Users\Koffi\Desktop\nasdaq\nasdaq\sipders\stocks.py
######Type (scrapy crawl nasdaq-o scraped.csv)This command runs scrapy and saves results as scraped csv file.
