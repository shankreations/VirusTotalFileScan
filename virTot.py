from virustotal_python import Virustotal

API_KEY="YOU API KEY HERE"


import os.path
from pprint import pprint

FILE_PATH = "/home/ubun/Downloads/240387329dee4f03f98a89a2feff9bf30dcba61fcf614cdac24129da54442762"

vtotal=Virustotal(API_KEY)
files = {"file": (os.path.basename(FILE_PATH), open(os.path.abspath(FILE_PATH), "rb"))}

resp = vtotal.request("file/scan", files=files, method="POST")

print(resp.response_code)
pprint(resp.json())

FILE_ID = "240387329dee4f03f98a89a2feff9bf30dcba61fcf614cdac24129da54442762-1615673445"

resp = vtotal.request("file/report", {"resource": FILE_ID})

print(resp.response_code)
pprint(resp.json())
