from pymongo import MongoClient
import json

def basic_merge():
    db = MongoClient().wb_datamerge_spike
    merged_collection = db.merged
    
    uk_collection = db.uk
    uk_contracts = uk_collection.contracts
    uk_contract_awards = uk_collection.contract_awards
    ph_collection = db.ph
    ph_contracts = ph_collection.contracts
    ph_contract_awards = ph_collection.contract_awards
    co_collection = db.co
    wb_collection = db.wb.contract_awards
    us_collection = db.us.transactions
    
    uk_contracts_map = {
        "category": "FD_CONTRACT.@CTYPE"
    }
    
    uk_contract_awards_map = {
        "category": "FD_CONTRACT_AWARD.@CTYPE"
    }
    
    ph_contracts_map = {
        "category": "classification"
    }
    
    ph_contract_awards_map = ph_contracts_map
    
    co_map = {
         "category": "TIPO_CONTRATO"
    }

    collections = [
        (uk_contracts, uk_contracts_map),
        (uk_contract_awards, uk_contract_awards_map),
        (ph_contracts, ph_contracts_map),
        (ph_contract_awards, ph_contract_awards_map),
        (co_collection, co_map)
#        (wb_collection, 'wb_contract_awards_map.json'),
#        (us_collection, 'us_partial_map.json')
    ]
    
    for collection in collections:        
        for record in collection[0].find():
            mapping = collection[1]
            mappingpieces = mapping['category'].split('.')
            mappedcategory = record
            for piece in mappingpieces:
                mappedcategory = mappedcategory[piece]
            newrecord = {
                "opencontract-activity": {
                    "meta": {
                        "category": mappedcategory, 
                    }
                }
            }
            merged_collection.insert(newrecord)
        
    
