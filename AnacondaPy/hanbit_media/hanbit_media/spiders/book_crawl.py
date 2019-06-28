# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookCrawlSpider(CrawlSpider):

    # 크롤러 명
    name = 'book_crawl'

    # 크롤러 실행을 허용할 도메인 지정
    # 해당 서버에서 실행되다가 허용오딘 도메인 이외는 무시
    allowed_domains = ['hanbit.co.kr']

    # 시작점 URL
    # 리스트로 지정해 한 번에 여러 웹 페이지에서 크롤링 시작 가능
    start_urls = ['http://hanbit.co.kr/store/books/category_list.html?cate_cd=001',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=002',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=003',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=004',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=005',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=006',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=007',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=008'
                  ]

    # 크롤러 작동 규칙 설정
    # 시작점의 모든 링크를 검사한 후,
    # 매개1 : 규칙
    # 매개2 : 규칙에 맞는 링크가 있으면 정해진 콜백 메소드 실행
    # 매개3 : follow=True로 설정되면, 해당 페이지의 링크를 대상으로 응답에 다시 한번 rules를 적용해 재귀적 앞 작업 반복 실행
    rules = (
        # 정규 표현식을 이용하여 크롤링할 링크 표현
        # store/books/look.php?p.code=B8463790401
        Rule(LinkExtractor(allow=r'store/books/look.php\?p.code=.*'),
            callback='parse_item', follow=True),
        # store/books/category_list.html?page=2&cate_cd=003&srt=p_pub_date
        Rule(LinkExtractor(allow=
                           r'store/books/category_list\.html\?page=\d+&cate_cd=00\d+&srt=p_pub_date'))
    )


    ''' rules를 통과한 링크에 요청을 보내 응답을 받으면 Rule()에 설정한 콜백메소드를 해당 응답 결과에 실행
        response를 파라미터로 받고, XPath 또는 CSS 선택자를 이용하여 원하는 요소 추출 가능
    '''
    def parse_item(self, response):
        i = {}

        i['book_title'] = \
            response.xpath(
                '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/h3/text()'
            ).extract()

        #저자
        i['book_author'] = \
            response.xpath(
                '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="저자 : "]/span/text()'
            ).extract()

        #번역자
        i['book_translator'] = \
            response.xpath(
                '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="번역 : "]/span/text()'
            ).extract()

        # 출간일
        i['book_pub_date'] = \
            response.xpath(
                '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="출간 : "]/span/text()'
            ).extract()

        i['book_isbn'] = \
            response.xpath(
                '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="ISBN : "]/span/text()'
            ).extract()

        return i
