import scrapy
from vgmusic.items import MidiFile

import re
slugify_strip_re = re.compile(r'[^\w\s-]')
slugify_hyphenate_re = re.compile(r'[-\s]+')
def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    
    From Django's "django/template/defaultfilters.py".
    """
    import unicodedata
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode()
    value = slugify_strip_re.sub('', value).strip().lower()
    return slugify_hyphenate_re.sub('_', value)

class QuotesSpider(scrapy.Spider):
    name = "vgmusic"

    def start_requests(self):
        yield scrapy.Request(url="https://www.vgmusic.com/", callback=self.parse)

    def parse(self, response):
        meta = response.meta
        brands = response.css('p.menularge::text, p.menuhead::text').extract()
        for idx in range(3, len(brands)):
            meta['brand'] = brands[idx].strip()
            urls = response.xpath('//p[count(preceding-sibling::p[contains(@class, "menularge") or contains(@class, "menuhead")]) = %d]/a'%(idx))
            for url in urls:
                meta['console_name'] = url.xpath('text()').extract_first()
                url = url.xpath('@href').extract_first()
                yield scrapy.Request(url=response.urljoin(url), callback=self.console_page, meta=meta)

    def console_page(self, response):
        meta = response.meta
        names = response.xpath('//td[contains(@class, "header")]//a/text()').extract()
        paths = response.xpath('//td[contains(@class, "header")]//a/@name').extract()
        for idx in range(len(paths)):
            game_name = names[idx]
            game_path = paths[idx]
            songs = response.xpath('//tr[(count(preceding-sibling::tr[contains(@class, "header")]//a/@name) = %d)]/td[not(@align) and not(contains(@class, "header"))]/a'%(idx+1))
            for song in songs:
                item = MidiFile()
                item['game'] = game_name
                item['console'] = meta['console_name']
                item['brand'] = meta['brand']
                item['title'] = song.xpath('text()').extract_first()
                item['file_urls'] = [response.urljoin(song.xpath('@href').extract_first())]
                item['file_path'] = "%s/%s/%s"%(slugify(meta['brand']),\
                                      slugify(meta['console_name']),\
                                      slugify(game_path))
                yield item
