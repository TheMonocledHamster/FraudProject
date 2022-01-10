import json
import os
import random
import re


PLANS_RANGE = 16
FEATURE_RANGE = 24
SUBS_RANGE = random.randint(5000,5500)
TRANS_RANGE = random.randint(10000,13000)
USE_RANGE = random.randint(80000,100000)


relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))
with open(relpath("../../Resources/DBdetails.json"),"r") as deets:
    PARAMS = json.load(deets)
with open(relpath("InitSchema.sql"),"r") as SCHEMA:
    SCHEMA = SCHEMA.read()
with open(relpath("AddForeignKeys.SQL"),"r") as FKeys:
    FKeys = FKeys.read()
with open(relpath("NewPlanFunction.SQL"),"r") as PC_FN:
    PC_FN = PC_FN.read()
with open(relpath("NewPlanTrigger.SQL"),"r") as PC_TRIG:
    PC_TRIG = PC_TRIG.read()
with open(relpath("DetectFraudFunction.SQL"),"r") as FT_FN:
    FT_FN = FT_FN.read()
with open(relpath("DetectFraudTrigger.SQL"),"r") as FT_TRIG:
    FT_TRIG = FT_TRIG.read()
with open(relpath("CheckFraudProc.SQL"),"r") as CF_PROC:
    CF_PROC = CF_PROC.read()
with open(relpath("FraudsView.SQL"),"r") as F_VIEW:
    F_VIEW = F_VIEW.read()
with open(relpath("FraudIndex.SQL"),"r") as IDX:
    IDX = IDX.read()


COUNTRIES = {
    "Belgium":32, 
    "Germany":49, 
    "Austria":43, 
    "France":33, 
    "Czech Republic":420, 
    "The Netherlands":31
    }
p_countries = [0.15, 0.25, 0.1, 0.2, 0.05, 0.25]


ACTIONS = ["Call","SMS","Video Call"]
p_actions = [0.45,0.45,0.1]

TRANS_TYPES = ["SIM Change","Plan Renewal","New Plan","Data Add-on","New Sub"]
p_trans = [0.01,0.60,0.05,0.14,0.2]



TABLES = ["plans", "subscribers", "features", "tracking", "transactions", "usage_data"]