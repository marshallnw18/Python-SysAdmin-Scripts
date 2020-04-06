#!/usr/bin/env python3.6

#import os library
import os 

#Use the os lib to check the "STAGE" environment variable
#If "STAGE" is not set, default value will be DEV environment
stage = os.getenv("STAGE", default="dev").upper()
output = f"We're running in {stage}"

#If script detects that we're in PROD, a warning will be issued
if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)