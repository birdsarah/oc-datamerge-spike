import json
import collections

def combinedicts(dict1, dict2):
    mergeddict = {}
    for k, v in dict1.iteritems():
        newv = {}
        for question, mapping in v.iteritems():
            if mapping == '':
                mapping = dict2[k][question]
            newv.update({question: mapping})        
        mergeddict.update({k: newv})
    return mergeddict

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
    maps = ['Colombia',
            'Philippines',
            'UK',
            'World Bank',
            'US (Partial)']

    alldata = collections.OrderedDict()
    for themap in maps:
        filename = 'consolidated/' + themap + '.json'
        with open(filename) as f:
            data = json.loads(f.read())
        alldata.update(flattenandaddnameandchildren(data, themap))
        sortedlist = sortthequestionlist(alldata)
        with open('alldata.json', 'w') as f:
            f.write(json.dumps(sortedlist, indent=4))
        
