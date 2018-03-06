# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request,FormRequest

class LjSpider(scrapy.Spider):
    name = 'lj'
    allowed_domains = ['douban.com']
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36login	jquery.min.js	blank.gif	connect_wechat.png	connect_sina_weibo.png	data:image/png;base…	hm.gif?si=3b231847743b9335bfaccda43a1abc1b&et=0&nv=0&st=4&v=pixel-1.0&rnd=709539161	"}
    def start_requests(self):
        return [Request("https://accounts.douban.com/login",headers=self.headers,meta={"cookiejar":1},callback=self.parse)]


    def parse(self, response):
        data={"form_email":"13021121977","form_password":"god496960","redir":"https://www.douban.com/people/164123288/"}
        return [FormRequest.from_response(response,meta={"cookiejar":response.meta["cookiejar"]},headers=self.headers,formdata=data,callback=self.next)]
    def next(self,response):
        title=response.xpath("/html/head/title/text()").extract()
        print("the title is"+title[0])
