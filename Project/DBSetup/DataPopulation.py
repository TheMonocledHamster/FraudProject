from faker import Faker
import psycopg2
import pandas as pd
import numpy as np
from collections import defaultdict
import random
import itertools
import Const


params = Const.PARAMS
pg_connection = psycopg2.connect(dbname=params["NAME"], user=params["USER"], password=params["PASSWORD"], host=params["HOST"], port=params["PORT"])
pg_connection.set_session(autocommit=True)
db_cursor = pg_connection.cursor()


fake = Faker()
fake_subscribers = defaultdict(list)
fake_transactions = defaultdict(list)
fake_plan = defaultdict(list)
fake_usage_data = defaultdict(list)
fake_features = defaultdict(list)


#FEATURES
""" Generate data and populate the features table with all possible combinations """
smsNo,ottChoice = [50,100,200],[True,False]
flist_vals = [smsNo]
flist_vals.extend([ottChoice]*3)
feature_list = list(itertools.product(*flist_vals))
for i in range(Const.FEATURE_RANGE):
    fake_features["feature_id"].append( i )
    fake_features["sms"].append( feature_list[i][0] )
    fake_features["netflix"].append( feature_list[i][1] )
    fake_features["primevideo"].append( feature_list[i][2] )
    fake_features["hotstar"].append( feature_list[i][3] )
df_fake_features = pd.DataFrame(fake_features)


#PLANS
""" Generate plans, calculate costs and populate plans table """
get_cost = lambda i : fake_plan["plan_data"][i] * fake_plan["validity"][i] * 0.5
for i in range(Const.PLANS_RANGE):
    fake_plan["plan_id"].append( i )
    fake_plan["plan_data"].append( random.randint(2,6)/2.0 )
    fake_plan["validity"].append( random.randint(15,360) )
    fake_plan["plan_cost"].append( get_cost(i) )
    fake_plan["feature_id"].append( None )
    fake_plan["postpaid"].append( np.random.choice([False,True],p=[0.75,0.25]) )
df_fake_plan = pd.DataFrame(fake_plan)

for i in range(Const.PLANS_RANGE):
    df_fake_plan.loc[i,'feature_id'] = np.random.choice(df_fake_features.index.tolist())


#SUBSCRIBERS
""" Generate subscriber identities for subs table """
avl_countries = {"Belgium":32, "Germany":49, "Austria":43, "France":33, "Poland":48, "The Netherlands":31}
for i in range(Const.SUBS_RANGE):
    fake_subscribers["sub_id"].append( i )
    fake_subscribers["full_name"].append( fake.name() )
    fake_subscribers["created_at"].append( fake.date_time_between(start_date='-17y', end_date='-10y') )
    fake_subscribers["country"].append( np.random.choice(list(avl_countries.keys()), p=[0.15, 0.2, 0.1, 0.2, 0.15, 0.2]) )
    fake_subscribers["phone_number"].append( '+' + str(avl_countries[fake_subscribers["country"][i]]) + ' ' \
        + str(random.randint(190,499)) + ' ' + str(random.randint(100,999)) + ' ' + str(random.randint(1000,9999)) )
    fake_subscribers["cur_plan_id"].append( None )
df_fake_subscribers = pd.DataFrame(fake_subscribers)


#USAGE
""" Generate actions to populate usage table """
avl_actions = ["Call","SMS","Video Call"]
p_actions = [0.45,0.45,0.1]
for i in range(Const.USE_RANGE):
    fake_usage_data["usage_id"].append( i )
    fake_usage_data["sub_id"].append( None )
    fake_usage_data["use_type"].append( np.random.choice(avl_actions,p=p_actions) )
    fake_usage_data["usage_time"].append( fake.date_time() )
    fake_usage_data["amount"].append( random.randint(1,60) )
df_fake_usage_data = pd.DataFrame(fake_usage_data)


#TRANSACTIONS
""" Generate transactions to populate user's transactions table """
avl_trans = ["SIM Change","Plan Renewal","New Plan","Data Add-on"]
p_trans = [0.05,0.65,0.2,0.1]
for i in range(Const.TRANS_RANGE):
    fake_transactions["trans_id"].append( i )
    fake_transactions["sub_id"].append( None )
    fake_transactions["trans_type"].append( np.random.choice(avl_trans,p=p_trans) )
    fake_transactions["created_at"].append( fake.date_time() )
    fake_transactions["country"].append( None ) #Fill this with sub_id's country
    fake_transactions["buy_plan_id"].append( None )
df_fake_transactions = pd.DataFrame(fake_transactions)



print(df_fake_features,df_fake_plan,df_fake_subscribers,df_fake_transactions,df_fake_usage_data,sep="\n\n")