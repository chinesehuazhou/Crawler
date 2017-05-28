# -*- coding: utf-8 -*-


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            # 如果该URL没有被/添加访问过就添加进管理器
            self.new_urls.add(url)
        pass

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            # 将URL列表添加进待访问队列
            self.new_urls.add(url)
        pass

    def has_new_url(self):
        # 返回URL池是否为空
        return len(self.new_urls) != 0
        pass

    def get_new_url(self):
        # 从未访问的URL中取出一个，并返回取出的URL
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
        pass
