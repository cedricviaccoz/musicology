# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem


class VgmusicPipeline(FilesPipeline):
    def filename(self, url):
        return url.rsplit('/', 1)[-1]

    def item_completed(self, results, item, info):
        for result in [x for ok, x in results if ok]:
            path = result['path']
            settings = get_project_settings()
            storage = settings.get('FILES_STORE')

            target_path = os.path.join(storage, item['file_path'], self.filename(item['file_urls'][0]))
            path = os.path.join(storage, path)

            # If path doesn't exist, it will be created
            if not os.path.exists(os.path.join(storage, item['file_path'])):
                os.makedirs(os.path.join(storage, item['file_path']))
            if not os.rename(path, target_path):
                raise DropItem("Could not move image from source: %s to target folder: %s"%(path, target_path))
        return item
