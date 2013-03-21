from pymongo import MongoClient
import xmltodict
import json


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

if __name__ == '__main__':
    db = MongoClient().wb_datamerge_spike
    enter_uk_data(db)
    enter_wb_data(db)
    enter_ph_data(db)
