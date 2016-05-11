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
    name = "aladdin58"
    allowed_domains = ["58.com"]
    start_urls = [
        "http://quanguo.58.com/chuanmei",
        "http://quanguo.58.com/hunjiehunqing/",
        "http://quanguo.58.com/shangwu/",
        "http://quanguo.58.com/zhaoshang/",
        "http://quanguo.58.com/shenghuo/",
        "http://quanguo.58.com/xiuxianyl/",
        "http://quanguo.58.com/liren/",
        "http://quanguo.58.com/jiaoyu/",
        "http://quanguo.58.com/jianshen",
        "http://quanguo.58.com/zuliaoam",
        "http://quanguo.58.com/spa",
        "http://quanguo.58.com/hunjiehunqing/",
        "http://quanguo.58.com/rjgcspeixun",
        "http://quanguo.58.com/pmshpeixun",
        "http://quanguo.58.com/mba",
        "http://quanguo.58.com/wlyxpeixun/",
        "http://quanguo.58.com/techang/",
        "http://quanguo.58.com/youjiao/",
        "http://quanguo.58.com/taijiao/",
        "http://quanguo.58.com/qinzijiaoyu/",
        "http://quanguo.58.com/youeryuanjiaoyu/",
        "http://quanguo.58.com/xueqianjiaoyu/",
        "http://quanguo.58.com/muyingyp/",
        "http://quanguo.58.com/huazhuangp/",
        "http://quanguo.58.com/shop/",
        "http://quanguo.58.com/xianhuasudi/",
        "http://quanguo.58.com/zhuangxiujc/",
        "http://quanguo.58.com/qichefw/",
        "http://quanguo.58.com/lvyouxiuxian/",
        "http://quanguo.58.com/canyin/",
        "http://quanguo.58.com/nonglinmy/",
        "http://quanguo.58.com/yiliaobaojian/"

    ]
    rules = [
        Rule(sle(allow=("/chuanmei/pn\d+")), follow=True, callback='parse_item'),
        Rule(sle(allow=("http://\w+.58.com/.+\.shtml")), follow=True, callback='parse_item')
    ]

    def parse_item(self, response):
        rand = random.randint(1, 2)
        time.sleep(rand)
        items = []
        sel = Selector(response)
        base_url = get_base_url(response)
        title_root_path = sel.css('.mainTitle')
        phone_root_path = sel.css('.l_phone')
        if title_root_path is None or len(title_root_path) == 0 or phone_root_path is None or len(phone_root_path) == 0:
            return items

        title_path = title_root_path.xpath('./h1/text()')
        phone_path = phone_root_path.xpath('text()')
        if title_path is not None and phone_path is not None:
            info_name = title_path
            item = AladdinItem()
            info_name_extract = info_name.extract()
            if info_name_extract is not None and len(info_name_extract) > 0:
                name = info_name_extract[0]
                item['name'] = name

            phone_extract = phone_path.extract()
            if phone_extract is not None and len(phone_extract) > 0:
                phone = phone_extract[0]
                phone_set = set()
                phone_set.add(phone)
                item['phone'] = phone_set

            if item.get('name') is not None and item.get('phone') is not None and len(set(item.get('phone'))) > 0:
                items.append(item)
        info(str(response))
        return items

    def _process_request(self, request):
        info('process ' + str(request))
        return request

