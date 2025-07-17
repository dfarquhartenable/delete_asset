# This program is a super simple but useful Pytenable script to delete an asset. Presented mostly as an example you can build on.
# enter the IPs you want to delete in line 16 (replace 192.168.1.83 and 75 with the ones you want

# This code is presented for example purposes and is unsupported.

from tenable.io import TenableIO
import getpass
import pprint

# get API keys from user (this prevents secrets from ending up in command history or worse yet, being hardcoded)
accesskey = getpass.getpass(prompt='Enter your access key for TVM: ')
secretkey = getpass.getpass(prompt='Enter your secret key for TVM: ')

# Initialize Tenable Vulnerability Management
tvm = TenableIO(accesskey, secretkey)

for ip in ("192.168.1.83", "192.168.1.75"):
    asset = tvm.assets.bulk_delete(('ipv4', 'eq', ip), hard_delete=True)
    print(ip)
    pprint.pprint(asset)
