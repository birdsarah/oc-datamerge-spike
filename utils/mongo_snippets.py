def linking_uk_data(db):
    """
    Expects a pymongo db object with collections uk.contract_awards & uk.contracts
    """
    queryset = db.uk.contract_awards.find({"SYSTEM.PARENT_NOTICE_ID": {"$ne": None}})
    linkedcount = 0
    linkedlist = []
    for record in queryset:
        linked = db.uk.contracts.find_one({"SYSTEM.NOTICE_ID": record["SYSTEM"]["PARENT_NOTICE_ID"]})
        if linked:                                
            linkedcount += 1       
            #print linked["SYSTEM"]["NOTICE_ID"]
            #print linked["SYSTEM"]["BUYER_GROUP_NAME"]
            linkedlist.append(linked["SYSTEM"]["NOTICE_ID"])
    print "%s results in queryset. %s linked." % (queryset.count(), linkedcount)
    return linkedlist


def buyer_and_org_are_different(queryset):
    linked = [record["SYSTEM"]["NOTICE_ID"] for record in queryset if record["SYSTEM"]["BUYER_GROUP_NAME"] != record["FD_CONTRACT_AWARD"]["CONTRACTING_AUTHORITY_INFORMATION"]["NAME_ADDRESSES_CONTACT_CONTRACT_AWARD"]["CA_CE_CONCESSIONAIRE_PROFILE"]["ORGANISATION"]]
    print linked
    return len(linked)
        
