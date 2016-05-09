# Scrapy settings for itzhaopin project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'aladdin'

SPIDER_MODULES = ['aladdin.spiders']
NEWSPIDER_MODULE = 'aladdin.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'aladdin (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'aladdin.pipelines.JsonWithEncodingAladdinPipeline': 300,
}

LOG_LEVEL = 'INFO'

