import scrapy

from example.items import MovieItem

class MovieSpider(scrapy.Spider):
    name = "imbdmoviespider"
    allowed_domains = ['imdb.com']
    start_urls = ('https://www.imdb.com/chart/top', )

    def parse(self, response):
        links = response.xpath('//tbody[@class="lister-list"]/tr/td[@class="titleColumn"]/a/@href').extract()
        i = 1
        for link in links:
            abs_url = response.urljoin(link)
            #
            url_next = '//*[@id="main"]/div/span/div/div/div[2]/table/tbody/tr['+str(i)+']/td[3]/strong/text()'
            rating = response.xpath(url_next).extract()
            if (i <+ len(links)):
                i=i+1
                yield scrapy.Request(abs_url, callback = self.parse_indetail, meta={'rating': rating} )

    

    def parse_indetail(self,response):

        item = MovieItem()
        #
        item['title'] = response.xpath('//div[@class="title_wrapper"]/h1/text()').extract()[0][:-1]
        item['directors'] = response.xpath('//div[@class="credit_summary_item"]/span[@itemprop="director"]/a/span/text()').extract()
        

        return item
        
        


#scrapy crawl imbdmoviespider -o movie.csv -t csv

#//*[@id="title-overview-widget"]/div[3]/div[1]/div[2]/a

        
        
    #//*[@id="main"]/div/span/div/div/div[3]/table/tbody
    #//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]/a
