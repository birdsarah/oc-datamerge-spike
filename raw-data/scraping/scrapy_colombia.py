from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import FormRequest, Request


class ColombiaSpider(BaseSpider):

    name = 'ColombiaSpider'
    allowed_domains = ['www.contratos.gov.co']
    start_urls = ['https://www.contratos.gov.co/consultas/inicioConsulta.do']

    def parse(self, response):
        return FormRequest.from_response(response,
                                         formname='parametros',
                                         formdata={
                                             'tipoProceso': '1',
                                             'estado': '1',
                                             'objeto': '',
                                             'registrosXPagina': '100',
                                         },
                                         callback=self.parse_results)

    def parse_results(self, response):
        print response.body
