import scrapy

from example.items import NewItem

class FirstSpider(scrapy.Spider):
    name = "FirstBlogSpider"
    allowed_domains = ['www.hamims-blog.herokuapp.com']
    start_urls = ['https://hamims-blog.herokuapp.com/']
    
    def parse(self, response):
        item = NewItem() #class created in items
        #item['main_headline']=response.xpath('//span/text()').extract()
        item['headline']=response.xpath('//title/text()').extract()
        item['url']=response.url
        item['project']=self.settings.get('BOT_NAME')
        item['spider']=self.name
    
        return item
        
   


        
            
        

    

     
            
        






        

