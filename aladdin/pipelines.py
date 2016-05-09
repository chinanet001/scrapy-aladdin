# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import codecs
import xlwt

class JsonWithEncodingAladdinPipeline(object):

    def __init__(self):
        #self.file = codecs.open('aladdin.json', 'w', encoding='utf-8')
        self.excel = xlwt.Workbook()
        self.table = self.excel.add_sheet('zbj', cell_overwrite_ok=True)
        self.table.write(0, 0, 'name')
        self.table.write(0, 1, 'phone')
        self.row = 1

    def process_item(self, item, spider):
        if item is None and len(item) == 0:
            return item
        #line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #self.file.write(line)
        data = dict(item)
        cell = 0
        for x in data.values():
            self.table.write(self.row, cell, x)
            cell += 1
        self.row += 1
        self.excel.save('aladdin.xls')
        return item

    def spider_closed(self, spider):
        self.excel.save('aladdin.xls')

