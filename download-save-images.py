import json
import requests
import eventlet
import shutil
import os.path

from eventlet import timeout

data = json.load(open('mapping.json'))

for key, value in data.items():
    try:
        filename = "down\\{}.jpg".format(key)

        if os.path.exists(filename):
            continue

        r = requests.get(value, verify=False, timeout=10, stream=True)

        if r.status_code == 200:
            with open(filename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except:
        continue

