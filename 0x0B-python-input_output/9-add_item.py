#!/usr/bin/python3
import json
from sys import argv
import os.path
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

FileName = "add_item.json"
if not os.path.exists(FileName):
    tmpFile = open(FileName, "w+")
    tmpFile.write(json.dumps([]))
    tmpFile.close()

JList = load_from_json_file(FileName)
for x in argv[1:]:
    JList.append(x)
save_to_json_file(JList, FileName)
