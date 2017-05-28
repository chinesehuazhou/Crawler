# -*- coding: utf-8 -*-
from imoocWebCrawler import URLManager, HTMLDownloader, HTMLParser, HTMLOutputer


class CrawlerMain(object):

    def __init__(self):
        self.urls = URLManager.UrlManager()                     # 初始化URL管理器
        self.downloader = HTMLDownloader.HtmlDownloader()       # 初始化HTML下载器
        self.parser = HTMLParser.HtmlParser()                   # 初始化HTML解析器
        self.outputer = HTMLOutputer.HtmlOutputer()             # 初始化HTML输出器
        pass

    def crawl(self, root_url):
        count = 1        # 爬取计数

        self.urls.add_new_url(root_url)                 # 将入口URL添加进管理器
        while self.urls.has_new_url():                  # 若URL池不为空则进行爬取
            try:
                new_url = self.urls.get_new_url()           # 获取要下载的URL
                print('crawl %d: %s' % (count, new_url))    # 打印正在爬取第几个页面及其URL
                html_cont = self.downloader.download(new_url)      # 下载页面
                new_urls, new_data = self.parser.hparse(
                    new_url, html_cont)  # 获取新的URL列表和页面数据
                self.urls.add_new_urls(new_urls)            # 将新的URL列表添加进管理器
                self.outputer.collect_data(new_data)        # 收集数据

                if count == 10:
                    break
                count = count + 1

            except:
                print('Crawl Failed')

        self.outputer.output_html()   # 将数据输出为HTML
        pass


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/item/Python"         # 入口URL
    obj_crawler = CrawlerMain()                             # 创建爬虫实例
    obj_crawler.crawl(root_url)                             # 调用爬虫方法
