#!/usr/bin/env python


from urllib.request import urlopen
import json


def fetchMD(drugName):
    try:
        return tuple(json.loads(urlopen('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/'+drugName.replace(" ", "%20")+'/property/molecularWeight,xlogp,complexity,tpsa/JSON').read().decode("utf-8"))['PropertyTable']['Properties'][0].values())[1:]
    except:
        return (None, None, None, None)
    # end try
print(fetchMD("valproic acid"))