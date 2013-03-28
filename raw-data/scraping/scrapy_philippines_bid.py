from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item, Field
from scrapy.http import Request


class PhilippinesBid(Item):
    ref_number = Field()
    procuring_entity = Field()
    title = Field()
    area_of_delivery = Field()  # lblDisplayAOD
    solicitation_number = Field()  # lblDisplaySolNumber
    trade_agreement = Field()  # lblDisplayTradeAgree
    procurement_mode = Field()  # lblDisplayProcureMode
    classification = Field()  # lblDisplayClass
    category = Field()  # lblDisplayCategory
    approved_budget = Field()  # lblDisplayBudget
    delivery_period = Field()  # lblDisplayPeriod
    client_agency = Field()  # lblDisplayClient
    contact_person = Field()  # lblDisplayContactPerson
    description = Field()  # lblAbstractText
    created_by = Field()  # lblDisplayCreatdBy
    date_created = Field()  # lblDisplayDateCreated
    status = Field()  # lblDisplayStatus
    supplements = Field()  # lblDisplayBidSupplements
    document_request_list = Field()  # lblDisplayDocReqList
    date_published = Field()  # lblDisplayDatePublish
    last_updated = Field()  # lblDisplayLastUpdateTime
    date_closing = Field()  # lblDisplayCloseDateTime

    xpath_mapping = {
        'ref_number': 'lblDisplayReferenceNo',
        'procuring_entity': 'lblDisplayProcuringEntity',
        'title': 'lblDisplayTitle',
        'area_of_delivery': 'lblDisplayAOD',
        'solicitation_number': 'lblDisplaySolNumber',
        'trade_agreement': 'lblDisplayTradeAgree',
        'procurement_mode': 'lblDisplayProcureMode',
        'classification': 'lblDisplayClass',
        'category': 'lblDisplayCategory',
        'approved_budget': 'lblDisplayBudget',
        'delivery_period': 'lblDisplayPeriod',
        'client_agency': 'lblDisplayClient',
        'contact_person': 'lblDisplayContactPerson',
        'description': 'lblAbstractText',
        'created_by': 'lblDisplayCreatdBy',
        'date_created': 'lblDisplayDateCreated',
        'status': 'lblDisplayStatus',
        'supplements': 'lblDisplayBidSupplements',
        'document_request_list': 'lblDisplayDocReqList',
        'date_published': 'lblDisplayDatePublish',
        'last_updated': 'lblDisplayLastUpdateTime',
        'date_closing': 'lblDisplayCloseDateTime',
    }


class PhilippinesSpider(CrawlSpider):
    name = "PhilippinesSpider"
    baseurl = "http://www.philgeps.gov.ph/GEPSNONPILOT/Tender/SplashBidNoticeAbstractUI.aspx?refID="
    allowed_domains = ['www.philgeps.gov.ph']
    start_urls = [baseurl + str(x) for x in range(2167788, 2167000, -1)]

    rules = (
        Rule(SgmlLinkExtractor(allow=('SplashBidNoticeAbstractUI\.aspx', )),
             callback='parse_detail'),
    )

    def parse_detail(self, response):
        self.response = response
        if response.status == 200:
            bid = PhilippinesBid()
            for k, v in bid.xpath_mapping.items():
                bid[k] = self.get_element_text(v)
            return bid
        return None

    def get_element_text(self, element_id):
        hxs = HtmlXPathSelector(self.response)
        xpath = '//*[@id="' + element_id + '"]/text()'
        try:
            value = hxs.select(xpath).extract()[0]
        except IndexError:
            value = None
        return value
