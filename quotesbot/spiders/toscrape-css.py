# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    # start_urls = [
    #     'http://www.oicq88.com'
    # 'http://www.oicq88.com/qinglv/1.htm',
    # 'http://www.oicq88.com/gexing/1.htm',
    # 'http://www.oicq88.com/feizhuliu/1.htm',
    # 'http://www.oicq88.com/yingwen/1.htm',
    # 'http://www.oicq88.com/shanggan/1.htm',
    # 'http://www.oicq88.com/nvsheng/1.htm',
    # 'http://www.oicq88.com/nansheng/1.htm',
    # 'http://www.oicq88.com/jiemei/1.htm',
    # 'http://www.oicq88.com/xiongdi/1.htm',
    # 'http://www.oicq88.com/weimei/1.htm',
    # 'http://www.oicq88.com/gaoxiao/1.htm',
    # 'http://www.oicq88.com/youxi/1.htm',
    # 'http://www.oicq88.com/chaozhuai/1.htm',
    # 'http://www.oicq88.com/baqi/1.htm',
    # 'http://www.oicq88.com/keai/1.htm',
    # 'http://www.oicq88.com/xiaoqingxin/1.htm',
    # 'http://www.oicq88.com/kongjian/1.htm',
    # 'http://www.oicq88.com/fantizi/1.htm',
    # 'http://www.oicq88.com/fuhao/1.htm',
    # 'http://www.oicq88.com/jingdian/1.htm',
    # 'http://www.oicq88.com/wenyi/1.htm',
    # 'http://www.oicq88.com/lizhi/1.htm',
    # 'http://www.oicq88.com/zhongkouwei/1.htm',
    # 'http://www.oicq88.com/gufeng/1.htm',
    # 'http://www.oicq88.com/jiandan/1.htm',
    # 'http://www.oicq88.com/shiyi/1.htm',
    # 'http://www.oicq88.com/neihan/1.htm',
    # 'http://www.oicq88.com/tuifei/1.htm',
    # 'http://www.oicq88.com/yijing/1.htm',
    # 'http://www.oicq88.com/shuaiqi/1.htm',
    # 'http://www.oicq88.com/jiazu/1.htm',
    # 'http://www.oicq88.com/chengshu/1.htm',
    # 'http://www.oicq88.com/geili/1.htm',
    # 'http://www.oicq88.com/youshang/1.htm',
    # 'http://www.oicq88.com/aiqing/1.htm',
    # 'http://www.oicq88.com/xiongmei/1.htm',
    # 'http://www.oicq88.com/xiaohai/1.htm',
    # 'http://www.oicq88.com/zhandui/1.htm',
    # ]

    def start_requests(self):
        urls = [
            'http://www.oicq88.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_categories)

    def parse_categories(self, response):
        categories = response.css('div.hd-tab')
        if categories is not None:
            category_pages = categories.css('a::attr(href)').extract()
            for page in category_pages:
                url = response.urljoin(page)
                yield scrapy.Request(url, callback=self.parse)
                url = response.urljoin(page + '1.htm')
                yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        print(response)
        for item in response.css('ul.list p::text').extract():
            yield {
                'name': item
            }
        next_page = response.css('div.page a.next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
