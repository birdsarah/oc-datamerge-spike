def blankdict(value):
    if isinstance(value, dict):
        return {k: blankdict(v) for k, v in value.iteritems()}
    elif isinstance(value, list):
        return blankdict(value[0])
    else:
        return ""


def writedict(dictionary, filename):
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(blankdict(dictionary), indent=4))


def updatekeys(dictionary, update):
    for k, v in update.iteritems():
        if type(v) == dict:
            newdictionary = dictionary.get(k, {})
            if type(newdictionary) == list:
                newdictionary = newdictionary[0]
            if type(newdictionary) == str:
                continue
            updatekeys(newdictionary, v)
        else:
            if not dictionary.get(k):
                dictionary[k] = v
    return dictionary


def makekeydict(collection):
    cache = {}
    for entry in collection:
        entryid = entry['_id']
        if not cache:
            cache = blankdict(collection.next())
        entry = blankdict(entry)
        updatekeys(entry, cache)
        cache = entry
    return entry


def countnestedkeys(dictionary, countlist=None):
    """
    Note, this doesn't count keys that are dictionaries inside a list.
    In that case we'd only want to count unique items probably - this gets tricky.
    This will also double count repeats at same level (although that's not valid json)
    """
    if not countlist:
        countlist = []
    countlist.append(len(dictionary.keys()))
    [countnestedkeys(v, countlist) for k, v in dictionary.iteritems() if type(v) == dict]
    return sum(countlist)


def countcommonitems(collection):
    import collections
    alldata = defaultdict(list)
    for record in collection:
        for k, v in record.iteritems():
            alldata[k].append(v)

    commonitems = {}
    for k, v in alldata.iteritems():
        countitems = collections.Counter(alldata[k])
        commontemp = {(key, value) for (key, value) in countitems.iteritems() if value > 1}
        commonitems.update({k: commontemp})
    return commonitems
