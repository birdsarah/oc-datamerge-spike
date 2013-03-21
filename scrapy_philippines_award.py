from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item, Field
from scrapy.http import Request


class PhilippinesAward(Item):
    ref_number = Field()
    title = Field()
    category = Field()  # Category
    solicitation_number = Field()  # SolNumber
    approved_budget = Field()  # Budget
    procuring_entity = Field()  # OrgName
    procuring_contact = Field()  # ContactName
    award_notice_number = Field()  # AwardNo
    award_notice_title = Field()  # AwardTitle
    reason_for_award = Field()  # Reason
    classification = Field()  # Class
    contract_number = Field()  # ContractNo
    supplier_name = Field()  # Awardees'
    supplier_address = Field()
    supplier_contact = Field()  # Contact
    supplier_contact_title = Field()  # CorpTitle
    status = Field()  # Status
    date_award = Field()  # AwardDate
    date_published = Field()  # PubDate
    components = Field()
    award_type = Field()  # AwardType
    contract_amount = Field()  # Amt
    date_proceed = Field()  # ProDate
    date_contract_start = Field()  # ContStartDate
    date_contract_end = Field()  # ContEndDate
    procurement_items = Field()
    url = Field()

    xpath_mapping = {
        'ref_number': 'lblDisplayRefNo',
        'title': 'lblDisplayTitle',
        'category': 'lblDisplayCategory',
        'solicitation_number': 'lblDisplaySolNumber',
        'approved_budget': 'lblDisplayBudget',
        'procuring_entity': 'lblDisplayOrgName',
        'procuring_contact': 'lblDisplayContactName',
        'award_notice_number': 'lblDisplayAwardNo',
        'award_notice_title': 'lblDisplayAwardTitle',
        'reason_for_award': 'lblDisplayReason',
        'classification': 'lblDisplayClass',
        'contract_number': 'lblDisplayContractNo',
        'supplier_name': 'lblDisplayAwardees',
        'supplier_address': 'lblDisplayAddress',
        'supplier_contact': 'lblDisplayContact',
        'supplier_contact_title': 'lblDisplayCorpTitle',
        'status': 'lblDisplayStatus',
        'date_award': 'lblDisplayAwardDate',
        'date_published': 'lblDisplayPubDate',
        'components': 'lblDisplayComp',
        'award_type': 'lblDisplayAwardType',
        'contract_amount': 'lblDisplayAmt',
        'date_proceed': 'lblDisplayProDate',
        'date_contract_start': 'lblDisplayContStartDate',
        'date_contract_end': 'lblDisplayContEndDate',
    }


class PhilippinesSpider(CrawlSpider):
    name = "PhilippinesSpider"
    baseurl = "http://www.philgeps.gov.ph/GEPSNONPILOT/Tender/SplashAwardNoticeAbstractUI.aspx?AwardID="
    allowed_domains = ['www.philgeps.gov.ph']
    start_urls = [baseurl + str(x) for x in range(436999, 436500, -1)]

    rules = (
        Rule(SgmlLinkExtractor(allow=('SplashAwardNoticeAbstractUI\.aspx', )),
             callback='parse_detail'),
    )

    def parse_detail(self, response):
        self.response = response
        if not self.get_element_text('ErrorDetailLabel'):
            award = PhilippinesAward()
            for k, v in award.xpath_mapping.items():
                award[k] = self.get_element_text(v)
            award['url'] = response.url
            return award
        return None

    def get_element_text(self, element_id):
        hxs = HtmlXPathSelector(self.response)
        xpath = '//*[@id="' + element_id + '"]/text()'
        try:
            value = hxs.select(xpath).extract()[0]
        except IndexError:
            value = None
        return value
