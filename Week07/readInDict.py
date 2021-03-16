# Reading in a file with Json

import json
filename="testdict.json"

def readDict():
    with open (filename) as f:
        return json.load (f)

somedict = readDict()
print(somedict)