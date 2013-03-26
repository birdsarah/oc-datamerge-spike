import json
import collections

def mergedictfiles(filenames):
    """
    Expects a list of filenames
    """
    mergeddict = {}
    for filename in filenames:
        with open(filename) as f:
            mergeddict.update(json.loads(f.read()))
    return mergeddict

def flattendict(tobeflat, root=None, tempdict=None):
    if not tempdict:
        tempdict = {}
    if not root:
        root = ''
    for k, v in tobeflat.iteritems():
        if type(v) != dict:
            newkey = "%s__%s" %(root, k)
            tempdict.update({newkey: v})
        else:
            flattendict(v, root=k, tempdict=tempdict)
    return tempdict

def putactivityandorgattoplevel(mergeddict, outfile=None):
    activity = mergeddict['opencontract-activity']
    org = mergeddict['opencontract-organization']

    together = activity
    together.update({"organization": org})

    #Remove unnecessary date obj
    if '@generated-datetime' in together:
        together.pop('@generated-datetime')

    flattenedtogether = {}    
    for k, v in together.iteritems():
        flattenedtogether.update({k: flattendict(v)})

    if outfile:
        with open(outfile, 'w') as f:
            f.write(json.dumps(flattenedtogether, indent=4))

    return flattenedtogether

def flattenandaddnameandchildren(startdict, startdictname):
    newdict = {startdictname: []}
    for k, v in startdict.iteritems():
        questionlist = []
        for questionkey, questionvalue in v.iteritems():
            if questionvalue:
                hasmap = "True"
            else:
                hasmap = "False"
            questiondict = {
                "questionkey": questionkey,
                "hasmap": hasmap
            }
            questionlist.append(questiondict)
        newdict[startdictname].append({"name": k, "children": questionlist})
    return newdict


def sortthequestionlist(processed):
    correctorder = [
        'organization',
        'meta',
        'bid',
        'award',
        'performance',
        'termination',
        'document'
    ]

    for country in processed:
        sortedlist = []
        for item in correctorder:
            for actual in processed[country]:
                if actual['name'] == item:
                    actualchildren = actual['children']
                    sortedactualchildren = sorted(actualchildren, key=lambda x:x['questionkey'])
                    sortedlist.append({"name": actual['name'], "children": sortedactualchildren})
                    break
        processed[country] = sortedlist
    return processed


if __name__ == '__main__':
    phca = mergedictfiles(['activity/ph_contract_awards_map.json', 'org/ph_contract_awards_map.json'])
    phc = mergedictfiles(['activity/ph_contracts_map.json', 'org/ph_contracts_map.json'])
    co = mergedictfiles(['activity/co_map.json', 'org/co_map.json'])
    ukc = mergedictfiles(['activity/uk_contracts_map.json', 'org/uk_contracts_map.json'])
    ukca =  mergedictfiles(['activity/uk_contract_awards_map.json', 'org/uk_contract_awards_map.json'])
    us =  mergedictfiles(['activity/us_partial_map.json', 'org/us_partial_map.json'])
    wb =  mergedictfiles(['activity/wb_contract_awards_map.json', 'org/wb_contract_awards_map.json'])
    
    maps = [
        {"World Bank": wb},
        {"Colombia": co},
        {"Philippines Awards": phca},
        {"Philippines Bids": phc},
        {"UK Bids": ukc},
        {"UK Awards": ukca},
        {"US (Partial)": us},
    ]

    alldata = collections.OrderedDict()
    for themap in maps:
        for k, v in themap.iteritems():
            filename = k + '.json'
            data =  putactivityandorgattoplevel(v, filename)
            alldata.update( flattenandaddnameandchildren(data, k))
        sortedlist = sortthequestionlist(alldata)
        with open('alldata.json', 'w') as f:
            f.write(json.dumps(sortedlist, indent=4))
        
