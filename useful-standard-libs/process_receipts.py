import os
import glob
import json
import shutil

#attempt to make the 'processed' directory
#if the directory already exists, catch the err and prompt user
try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already exists")

#create a list of receipt filepaths matching the glob pattern:
#starting with a number (0-9) and ending with a json file extensino
receipts = glob.glob('./new/receipt-[0-9]*.json')
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split("/")[-1]
    destination = f"./processed/{name}"
    shutil.move(path, destination)
    print(f"Moved {path} to {destination}")

print("Receipt subtotal: $%.2f" % subtotal)