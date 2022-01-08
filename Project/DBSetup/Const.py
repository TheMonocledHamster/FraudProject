import json
import os
import random


PLANS_RANGE = 16
FEATURE_RANGE = 24
SUBS_RANGE = random.randint(3000,4000)
TRANS_RANGE = random.randint(10000,13000)
USE_RANGE = random.randint(50000,60000)


relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))
with open(relpath("../../Resources/DBdetails.json"),"r") as deets:
    PARAMS = json.load(deets)
with open(relpath("InitSchema.sql"),"r") as SCHEMA:
    SCHEMA = SCHEMA.read()
with open(relpath("AddForeignKeys.SQL"),"r") as FKeys:
    FKeys = FKeys.read()


COUNTRIES = {
    "Belgium":32, 
    "Germany":49, 
    "Austria":43, 
    "France":33, 
    "Poland":48, 
    "The Netherlands":31
    }
p_countries = [0.15, 0.2, 0.1, 0.2, 0.15, 0.2]


ACTIONS = ["Call","SMS","Video Call"]
p_actions = [0.45,0.45,0.1]

TRANS_TYPES = ["SIM Change","Plan Renewal","New Plan","Data Add-on","New Sub"]
p_trans = [0.01,0.60,0.05,0.14,0.2]



TABLES = ["plans", "subscribers", "features", "tracking", "transactions", "usage_data"]