from virustotal_python import Virustotal
import os.path
from pprint import pprint

API_KEY="YOUR API KEY HERE"
FILE_PATH = "FULL PATH TO THE FILE"
vtotal=Virustotal(API_KEY)
files = {"file": (os.path.basename(FILE_PATH), open(os.path.abspath(FILE_PATH), "rb"))}
resp = vtotal.request("file/scan", files=files, method="POST")
print(resp.response_code)
pprint(resp.json())
SCAN_ID = "ENTER YOUR SCAN ID HERE"
resp = vtotal.request("file/report", {"resource": SCAN_ID})
print(resp.response_code)
pprint(resp.json())
