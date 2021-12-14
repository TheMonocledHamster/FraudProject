from faker import Faker
from numpy import NaN
import pandas as pd
from collections import defaultdict
import random


fake = Faker()
fake_subscribers = defaultdict(list)
fake_transactions = defaultdict(list)
fake_plan = defaultdict(list)
fake_usage_data = defaultdict(list)
fake_features = defaultdict(list)

for _ in range(5):
    fake_subscribers["full_name"].append( fake.name() )
    fake_subscribers["created_at"].append( fake.date_time() )
    fake_subscribers["country"].append( fake.country() )
    fake_subscribers["phone_number"].append( random.randint(1000000000,9999999999) )
    fake_subscribers["cur_plan_id"].append( None )

for _ in range(7):
    fake_transactions["sub_id"].append( None )
    fake_transactions["trans_type"].append( random.choice(["SIM Change","Plan Renewal","New Plan","Data Add-on"]) )
    fake_transactions["created_at"].append( fake.date_time() )
    fake_transactions["country"].append( None ) #Fill this with sub_id's country
    fake_transactions["buy_plan_id"].append( None )

for i in range(10):
    fake_plan["plan_data"].append( random.randint(2,6)/2.0 )
    fake_plan["validity"].append( random.randint(15,360) )
    fake_plan["plan_cost"].append( fake_plan["plan_data"][i] * fake_plan["validity"][i] * 3.0 )
    fake_plan["feature_id"].append( None )
    fake_plan["postpaid"].append( random.choice([False,False,False,True]) )

for _ in range(20):
    fake_usage_data["sub_id"].append( None )
    fake_usage_data["use_type"].append( random.choice(["Call","SMS","Video Call","Call","SMS","Call","SMS"]) )
    fake_usage_data["usage_time"].append( fake.date_time() )
    fake_usage_data["amount"].append( random.randint(1,60) )

for _ in range(50):
    fake_features["sms"].append( random.choice([50,100,200]) )
    fake_features["netflix"].append( random.choice([True,False]) )
    fake_features["primevideo"].append( random.choice([True,False]) )
    fake_features["hotstar"].append( random.choice([True,False]) )

df_fake_subscribers = pd.DataFrame(fake_subscribers)
# print(df_fake_subscribers)
df_fake_transactions = pd.DataFrame(fake_transactions)
# print(df_fake_transactions)
df_fake_plan = pd.DataFrame(fake_plan)
# print(df_fake_plan)
df_fake_usage_data = pd.DataFrame(fake_usage_data)
# print(df_fake_usage_data)
df_fake_features = (pd.DataFrame(fake_features)).drop_duplicates()
# print(df_fake_features)