# -*- coding: utf-8 -*-

from urllib import request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        # 打开网页
        response = request.urlopen(url)

        if response.getcode() != 200:
            # 打开失败返回None
            return None
        else:
            # 打开成功返回网页内容
            return response.read().decode("utf-8")
