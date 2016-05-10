import re
import json
import time
import random


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from aladdin.items import *
from aladdin.misc.log import *


class AladdinSpider(CrawlSpider):
    name = "aladdin"
    allowed_domains = ["zbj.com"]
    start_urls = [
        "http://www.zbj.com/ppsj/p.html",
        #"http://www.zbj.com/wdfw/p.html",
        #"http://www.zbj.com/yidongui/p.html",
        #"http://www.zbj.com/uisheji/pp10.html",
        #"http://www.zbj.com/rjkf/p.html",
        #"http://www.zbj.com/cyqm/p.html",
        #"http://www.zbj.com/sysx/p.html",
        #"http://www.zbj.com/yxtg/p.html",
        #"http://www.zbj.com/qyfw/p.html",
        #"http://www.zbj.com/ys/p.html",
        #"http://www.zbj.com/consult/p.html"
    ]
    rules = [
        Rule(sle(allow=("shop.zbj.com/\d+$")), follow=True, callback='parse_item'),
        Rule(sle(allow=("/ppsj/pp\d+.html")), follow=True, callback='parse_item'),
        #Rule(sle(allow=("shop.zbj.com/11463343/")), follow=True, callback='parse_item')
    ]

    def parse_item(self, response):
        rand = random.randint(2, 4)
        time.sleep(rand)
        items = []
        sel = Selector(response)
        base_url = get_base_url(response)
        root_path = sel.css('.shop-fixed-im-hover.shop-fixed-im-hover')
        if root_path is not None:
            info_name = root_path.xpath('./div[@class="shop-fixed-im-name"]/div[@class="fix-im-cate"]/text()')
            if info_name is not None:
                item = AladdinItem()
                info_name_extract = info_name.extract();
                if info_name_extract is not None and len(info_name_extract) > 0:
                    name = info_name_extract[0]
                    item['name'] = name
                    info_phones = root_path.xpath('./div[@class="shop-fix-im-time"]'
                                                  '/div[@class="fix-im-cate"]/following-sibling::*')
                    if info_phones is not None:
                        phone_set = set()
                        for info_phone in info_phones:
                            if info_phone.xpath('text()') is not None:
                                phone_extract = info_phone.xpath('text()').extract()
                                if phone_extract is not None and len(phone_extract) > 0:
                                    phone = phone_extract[0].strip()
                                    phone_set.add(phone)
                        item['phone'] = phone_set
            if item.get('name') is not None and item.get('phone') is not None:
                items.append(item)
        info(str(response))
        return items

    def _process_request(self, request):
        info('process ' + str(request))
        return request

