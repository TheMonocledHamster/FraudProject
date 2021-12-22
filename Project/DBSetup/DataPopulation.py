from faker import Faker
import psycopg2
import pandas as pd
from collections import defaultdict
import random
import itertools


fake = Faker()
fake_subscribers = defaultdict(list)
fake_transactions = defaultdict(list)
fake_plan = defaultdict(list)
fake_usage_data = defaultdict(list)
fake_features = defaultdict(list)


""" Generate data and populate the features table with all possible combinations """
smsNo,ottChoice = [50,100,200],[True,False]
flist_vals = [smsNo]
flist_vals.extend([ottChoice]*3)
feature_list = list(itertools.product(*flist_vals))
for i in range(24):
    fake_features["sms"].append( feature_list[i][0] )
    fake_features["netflix"].append( feature_list[i][1] )
    fake_features["primevideo"].append( feature_list[i][2] )
    fake_features["hotstar"].append( feature_list[i][3] )


""" Generate subscriber identities for subs table """
for _ in range(10):
    fake_subscribers["full_name"].append( fake.name() )
    fake_subscribers["created_at"].append( fake.date_time() )
    fake_subscribers["country"].append( fake.country() )
    fake_subscribers["phone_number"].append( random.randint(1000000000,9999999999) )
    fake_subscribers["cur_plan_id"].append( None )


""" Generate transactions to populate user's transactions table """
avl_trans = ["SIM Change","Plan Renewal","New Plan","Data Add-on"]
for _ in range(5):
    fake_transactions["sub_id"].append( None )
    fake_transactions["trans_type"].append( random.choice(avl_trans) )
    fake_transactions["created_at"].append( fake.date_time() )
    fake_transactions["country"].append( None ) #Fill this with sub_id's country
    fake_transactions["buy_plan_id"].append( None )


""" Generate plans, calculate costs and populate plans table """
get_cost = lambda i : fake_plan["plan_data"][i] * fake_plan["validity"][i] * 3.0
for i in range(10):
    fake_plan["plan_data"].append( random.randint(2,6)/2.0 )
    fake_plan["validity"].append( random.randint(15,360) )
    fake_plan["plan_cost"].append( get_cost(i) )
    fake_plan["feature_id"].append( None )
    fake_plan["postpaid"].append( random.choice([False,False,False,True]) )


""" Generate actions to populate usage table """
avl_actions = ["Call","SMS","Video Call"]
avl_actions.extend(["Call","SMS"]*3)
for _ in range(50):
    fake_usage_data["sub_id"].append( None )
    fake_usage_data["use_type"].append( random.choice(avl_actions) )
    fake_usage_data["usage_time"].append( fake.date_time() )
    fake_usage_data["amount"].append( random.randint(1,60) )


df_fake_subscribers = pd.DataFrame(fake_subscribers)
df_fake_transactions = pd.DataFrame(fake_transactions)
df_fake_plan = pd.DataFrame(fake_plan)
df_fake_usage_data = pd.DataFrame(fake_usage_data)
df_fake_features = pd.DataFrame(fake_features)