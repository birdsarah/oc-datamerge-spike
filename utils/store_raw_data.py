from pymongo import MongoClient
import xmltodict
import json
from csv import DictReader


def enter_uk_data(db):
    with open('data/uk.xml') as f:
        parsed = xmltodict.parse(f)

    uk_collection = db.uk

    contract_list = parsed['NOTICES']['CONTRACT']
    contract_award_list = parsed['NOTICES']['CONTRACT_AWARD']
    prior_information_list = parsed['NOTICES']['PRIOR_INFORMATION']

    for contract in contract_list:
        uk_collection.contracts.insert(contract)

    for contract_award in contract_award_list:
        uk_collection.contract_awards.insert(contract_award)

    for prior_information in prior_information_list:
        uk_collection.prior_informations.insert(prior_information)


def enter_wb_data(db):
    with open('data/wb-data.json') as f:
        j = json.loads(f.read())

    wb_collection = db.wb

    data_list = j['data']

    for data in data_list:
        data_json = {
            'as_of_date': data[8],
            'fiscal_year': data[9],
            'region': data[10],
            'borrower_country': data[11],
            'borrower_country_code': data[12],
            'project_id': data[13],
            'project_name': data[14],
            'procurement_type': data[15],
            'procurement_category': data[16],
            'procurement_method': data[17],
            'product_line': data[18],
            'wb_contract_number': data[19],
            'major_sector': data[20],
            'contract_description': data[21],
            'contract_signing_date': data[22],
            'supplier': data[23],
            'supplier_country': data[24],
            'supplier_country_code': data[25],
            'total_contract_amount': data[26],
            'borrower_contract_reference': data[27],
        }
        wb_collection.contract_awards.insert(data_json)


def enter_ph_data(db):
    with open('data/philippines_awards.json') as f:
        awards_list = f.read().splitlines()

    with open('data/philippines_bids.json') as f:
        bids_list = f.read().splitlines()

    ph_collection = db.ph

    for award in awards_list:
        award_json = json.loads(award)
        ph_collection.contract_awards.insert(award_json)

    for bid in bids_list:
        bid_json = json.loads(bid)
        ph_collection.contracts.insert(bid_json)


def enter_co_data(db):
    cofieldnames = ['NIVEL',
                    'ORDEN',
                    'NIT_ENTIDAD',
                    'NOMBRE_ENTIDAD',
                    'TIPO_MODALIDAD',
                    'NUMERO_CONSTANCIA',
                    'ID_OBJETO_CONTRATO',
                    'OBJETO_CONTRATO',
                    'DETALLE_OBJETO',
                    'TIPO_CONTRATO',
                    'CUANTIA',
                    'VALOR_DEFINITIVO',
                    'FECHACREACION',
                    'FECHAESTADOBORRADOR',
                    'FECHAESTADODESCARTADO',
                    'FECHAESTADOCONVOCADO',
                    'FECHAESTADOADJUDICADO',
                    'FECHAESTADOTERMANORMALDESPCONV',
                    'FECHAESTADOTERMANORMALDESPCONV_1',
                    'FECHAESTADOTERMANORMALDESPCONV_2',
                    'FECHAESTADOTERMANORMALDESPCONV_3',
                    'ESTADO_PROCESO',
                    'NOMBRE_CONTRATISTA',
                    'NIT_CONTRATISTA',
                    'FECHA_FIRMA_CONTRATO',
                    'VALOR_CONTRATO',
                    'VALOR_ADICIONES',
                    'url']

    co_collection = db.co
    with open('data/Colombia_data_utf8.csv') as f:
        codict = DictReader(f, fieldnames=cofieldnames)
        for row in codict:
            co_collection.insert(row)


def enter_us_data(db):
    usfieldnames = ['unique_transaction_id',
                     'transaction_status',
                     'obligatedamount',
                     'baseandexercisedoptionsvalue',
                     'baseandalloptionsvalue',
                     'maj_agency_cat',
                     'mod_agency',
                     'maj_fund_agency_cat',
                     'contractingofficeagencyid',
                     'contractingofficeid',
                     'fundingrequestingagencyid',
                     'fundingrequestingofficeid',
                     'fundedbyforeignentity',
                     'signeddate',
                     'effectivedate',
                     'currentcompletiondate',
                     'ultimatecompletiondate',
                     'lastdatetoorder',
                     'contractactiontype',
                     'reasonformodification',
                     'typeofcontractpricing',
                     'priceevaluationpercentdifference',
                     'subcontractplan',
                     'lettercontract',
                     'multiyearcontract',
                     'performancebasedservicecontract',
                     'majorprogramcode',
                     'contingencyhumanitarianpeacekeepingoperation',
                     'contractfinancing',
                     'costorpricingdata',
                     'costaccountingstandardsclause',
                     'descriptionofcontractrequirement',
                     'purchasecardaspaymentmethod',
                     'numberofactions',
                     'nationalinterestactioncode',
                     'progsourceagency',
                     'progsourceaccount',
                     'progsourcesubacct',
                     'account_title',
                     'rec_flag',
                     'typeofidc',
                     'multipleorsingleawardidc',
                     'programacronym',
                     'vendorname',
                     'vendoralternatename',
                     'vendorlegalorganizationname',
                     'vendordoingasbusinessname',
                     'divisionname',
                     'divisionnumberorofficecode',
                     'vendorenabled',
                     'vendorlocationdisableflag',
                     'ccrexception',
                     'streetaddress',
                     'streetaddress2',
                     'streetaddress3',
                     'city',
                     'state',
                     'zipcode',
                     'vendorcountrycode',
                     'vendor_state_code',
                     'vendor_cd',
                     'congressionaldistrict',
                     'vendorsitecode',
                     'vendoralternatesitecode',
                     'dunsnumber',
                     'parentdunsnumber',
                     'phoneno',
                     'faxno',
                     'registrationdate',
                     'renewaldate',
                     'mod_parent',
                     'locationcode',
                     'statecode',
                     'pop_state_code',
                     'placeofperformancecountrycode',
                     'placeofperformancezipcode',
                     'pop_cd',
                     'placeofperformancecongressionaldistrict',
                     'psc_cat',
                     'productorservicecode',
                     'systemequipmentcode',
                     'claimantprogramcode',
                     'principalnaicscode',
                     'informationtechnologycommercialitemcategory',
                     'gfe_gfp',
                     'useofepadesignatedproducts',
                     'recoveredmaterialclauses',
                     'seatransportation',
                     'contractbundling',
                     'consolidatedcontract',
                     'countryoforigin',
                     'placeofmanufacture',
                     'manufacturingorganizationtype',
                     'agencyid',
                     'piid',
                     'modnumber',
                     'transactionnumber',
                     'fiscal_year',
                     'idvagencyid',
                     'idvpiid',
                     'idvmodificationnumber',
                     'solicitationid',
                     'extentcompeted',
                     'reasonnotcompeted',
                     'numberofoffersreceived',
                     'commercialitemacquisitionprocedures',
                     'commercialitemtestprogram',
                     'smallbusinesscompetitivenessdemonstrationprogram',
                     'a76action',
                     'competitiveprocedures',
                     'solicitationprocedures',
                     'typeofsetaside',
                     'localareasetaside',
                     'evaluatedpreference',
                     'fedbizopps',
                     'research',
                     'statutoryexceptiontofairopportunity',
                     'organizationaltype',
                     'numberofemployees',
                     'annualrevenue',
                     'firm8aflag',
                     'hubzoneflag',
                     'sdbflag',
                     'issbacertifiedsmalldisadvantagedbusiness',
                     'shelteredworkshopflag',
                     'hbcuflag',
                     'educationalinstitutionflag',
                     'womenownedflag',
                     'veteranownedflag',
                     'srdvobflag',
                     'localgovernmentflag',
                     'minorityinstitutionflag',
                     'aiobflag',
                     'stategovernmentflag',
                     'federalgovernmentflag',
                     'minorityownedbusinessflag',
                     'apaobflag',
                     'tribalgovernmentflag',
                     'baobflag',
                     'naobflag',
                     'saaobflag',
                     'nonprofitorganizationflag',
                     'isothernotforprofitorganization',
                     'isforprofitorganization',
                     'isfoundation',
                     'haobflag',
                     'ishispanicservicinginstitution',
                     'emergingsmallbusinessflag',
                     'hospitalflag',
                     'contractingofficerbusinesssizedetermination',
                     'is1862landgrantcollege',
                     'is1890landgrantcollege',
                     'is1994landgrantcollege',
                     'isveterinarycollege',
                     'isveterinaryhospital',
                     'isprivateuniversityorcollege',
                     'isschoolofforestry',
                     'isstatecontrolledinstitutionofhigherlearning',
                     'isserviceprovider',
                     'receivescontracts',
                     'receivesgrants',
                     'receivescontractsandgrants',
                     'isairportauthority',
                     'iscouncilofgovernments',
                     'ishousingauthoritiespublicortribal',
                     'isinterstateentity',
                     'isplanningcommission',
                     'isportauthority',
                     'istransitauthority',
                     'issubchapterscorporation',
                     'islimitedliabilitycorporation',
                     'isforeignownedandlocated',
                     'isarchitectureandengineering',
                     'isdotcertifieddisadvantagedbusinessenterprise',
                     'iscitylocalgovernment',
                     'iscommunitydevelopedcorporationownedfirm',
                     'iscommunitydevelopmentcorporation',
                     'isconstructionfirm',
                     'ismanufacturerofgoods',
                     'iscorporateentitynottaxexempt',
                     'iscountylocalgovernment',
                     'isdomesticshelter',
                     'isfederalgovernmentagency',
                     'isfederallyfundedresearchanddevelopmentcorp',
                     'isforeigngovernment',
                     'isindiantribe',
                     'isintermunicipallocalgovernment',
                     'isinternationalorganization',
                     'islaborsurplusareafirm',
                     'islocalgovernmentowned',
                     'ismunicipalitylocalgovernment',
                     'isnativehawaiianownedorganizationorfirm',
                     'isotherbusinessororganization',
                     'isotherminorityowned',
                     'ispartnershiporlimitedliabilitypartnership',
                     'isschooldistrictlocalgovernment',
                     'issmallagriculturalcooperative',
                     'issoleproprietorship',
                     'istownshiplocalgovernment',
                     'istriballyownedfirm',
                     'istribalcollege',
                     'isalaskannativeownedcorporationorfirm',
                     'iscorporateentitytaxexempt',
                     'iswomenownedsmallbusiness',
                     'isecondisadvwomenownedsmallbusiness',
                     'isjointventurewomenownedsmallbusiness',
                     'isjointventureecondisadvwomenownedsmallbusiness',
                     'walshhealyact',
                     'servicecontractact',
                     'davisbaconact',
                     'clingercohenact',
                     'otherstatutoryauthority',
                     'interagencycontractingauthority']
    us_collection = db.us
    with open('data/us_data_sample.csv') as f:
        usdict = DictReader(f, fieldnames=usfieldnames)
        for row in usdict:
            us_collection.transactions.insert(row)  


if __name__ == '__main__':
    db = MongoClient().wb_datamerge_spike
    enter_uk_data(db)
    enter_wb_data(db)
    enter_ph_data(db)
    enter_co_data(db)
    enter_us_data(db)
