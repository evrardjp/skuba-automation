#!/usr/bin/env python
# That's very ugly you know.

import subprocess
import json
import sys

tfcall = subprocess.Popen(['terraform', 'output', '-json'],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
tfout,tferr = tfcall.communicate()

tfdata = json.loads(tfout)

inventory = dict()
inventory["_meta"]={"hostvars": {}}
inventory["all"]={"children": ["ungrouped", "masters", "workers"]}
inventory["masters"]={"hosts": []}
inventory["workers"]={"hosts": []}
inventory["ungrouped"]={"hosts": []}


for name, ip in tfdata['ip_masters']['value'].items():
    inventory["_meta"]["hostvars"][name] = { "ansible_user" : "sles", "ansible_host": ip, "ansible_become": "yes", "ansible_become_method": "sudo" }
    inventory["masters"]["hosts"].append(name)

for name, ip in tfdata['ip_workers']['value'].items():
    inventory["_meta"]["hostvars"][name] = { "ansible_user" : "sles", "ansible_host": ip, "ansible_become": "yes", "ansible_become_method": "sudo" }
    inventory["workers"]["hosts"].append(name)
print(inventory)
