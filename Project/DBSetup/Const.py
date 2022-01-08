import json
import os


PLANS_RANGE = 8
FEATURE_RANGE = 24
SUBS_RANGE = 10
TRANS_RANGE = 40
USE_RANGE = 50


relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))
with open(relpath("../../Resources/DBdetails.json"),"r") as deets:
    PARAMS = json.load(deets)


with open(relpath("../../Resources/InitSchema.sql"),"r") as SCHEMA:
    SCHEMA = SCHEMA.read()