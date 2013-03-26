import json
import collections

def sortthequestionlist(processed):
    correctorder = [
        'organization',
        'meta',
        'bid',
        'award',
        'performance',
        'termination',
        'document',
        'extra'
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
    

def flattenandaddnameandchildren(startdict, startdictname):
    newdict = {startdictname: []}
    for k, v in startdict.iteritems():
        questionlist = []
        for questionkey, questionvalue in v.iteritems():
            questiondict = {}
            if k == "extra":
                #For extra only include those values that do not have a map
                if questionvalue == "None":
                    questiondict = {
                        "questionkey": questionkey,
                    }  
            else:
                if questionvalue:
                    hasmap = "True"
                else:
                    hasmap = "False"
                questiondict = {
                    "questionkey": questionkey,
                    "hasmap": hasmap
                }
            if questiondict:
                questionlist.append(questiondict)
        newdict[startdictname].append({"name": k, "children": questionlist})
    return newdict


if __name__ == '__main__':
    alldata = collections.OrderedDict()
    filename = 'Blank.json'
    with open(filename) as f:
        data = json.loads(f.read())
    alldata.update(flattenandaddnameandchildren(data, "Blank"))
    sortedlist = sortthequestionlist(alldata)
    with open('alldata.json', 'w') as f:
        f.write(json.dumps(sortedlist, indent=4))
        
