from faker import Faker
import pandas as pd
import numpy as np
from collections import defaultdict
import random
import itertools
import psycopg2
import psycopg2.extras as extras
import Const


fake = Faker()
fake_subscribers = defaultdict(list)
fake_transactions = defaultdict(list)
fake_plans = defaultdict(list)
fake_usage_data = defaultdict(list)
fake_features = defaultdict(list)
fake_tracking = defaultdict(list)
new_subs = defaultdict(list)


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
get_cost = lambda i : round(fake_plans["plan_data"][i] * fake_plans["validity"][i] * 5, -1) - 1
for i in range(Const.PLANS_RANGE):
    fake_plans["plan_id"].append( i )
    fake_plans["plan_data"].append( random.randint(2,6)/2.0 )
    fake_plans["validity"].append( round(random.randint(15,360),-1) )
    fake_plans["plan_cost"].append( get_cost(i) )
    fake_plans["feature_id"].append( np.random.choice(df_fake_features.index.tolist()) )
    fake_plans["postpaid"].append( np.random.choice([False,True],p=[0.75,0.25]) )
df_fake_plans = pd.DataFrame(fake_plans)


#SUBSCRIBERS
""" Generate subscriber identities for subs table """
avl_countries = Const.COUNTRIES
p_countries = Const.p_countries
for i in range(Const.SUBS_RANGE):
    fake_subscribers["sub_id"].append( i )
    fake_subscribers["full_name"].append( fake.name() )
    fake_subscribers["created_at"].append( fake.date_time_between(start_date='-9y', end_date='-4y') )
    fake_subscribers["country"].append( np.random.choice(list(avl_countries.keys()), p=p_countries) )
    fake_subscribers["phone_no"].append( '+' + str(avl_countries[fake_subscribers["country"][i]]) + ' ' \
        + str(random.randint(190,499)) + ' ' + str(random.randint(100,999)) + ' ' + str(random.randint(1000,9999)) )
    fake_subscribers["cur_plan_id"].append( np.random.choice(df_fake_plans.index.tolist()) )
df_fake_subscribers = pd.DataFrame(fake_subscribers)


#TRANSACTIONS
""" Generate transactions to populate user's transactions table """
avl_trans = Const.TRANS_TYPES
p_trans = Const.p_trans
tracklist = []
j = df_fake_subscribers.shape[0]

fake_transactions["trans_id"].append( 0 )
fake_transactions["sub_id"].append( 0 )
fake_transactions["trans_type"].append( avl_trans[1] )
fake_transactions["created_at"].append( fake.date_time_between(start_date='-4y', end_date='now') )
fake_transactions["country"].append( df_fake_subscribers.loc[0,"country"] )
fake_transactions["buy_plan_id"].append( df_fake_subscribers.loc[0,"cur_plan_id"] )
fake_transactions["is_fraud"].append( False )

for i in range(1,Const.TRANS_RANGE):
    fake_transactions["trans_type"].append( np.random.choice(avl_trans, p=p_trans) )
    fake_transactions["created_at"].append( fake.date_time_between(start_date='-4y', end_date='now') )
    fake_transactions["trans_id"].append( i )
    fake_transactions["is_fraud"].append( False )
    if fake_transactions["trans_type"][i]  != "New Sub":
        fake_transactions["sub_id"].append( np.random.choice(df_fake_subscribers["sub_id"].tolist()) )
        fake_transactions["country"].append( df_fake_subscribers.loc[fake_transactions["sub_id"][i],"country"] )
        if fake_transactions["trans_type"][i] == "New Plan":
            fake_transactions["buy_plan_id"].append( np.random.choice(df_fake_plans.index.tolist()) )
            tracklist.append(i)
        else:
            fake_transactions["buy_plan_id"].append( df_fake_subscribers.loc[fake_transactions["sub_id"][i],"cur_plan_id"] )
    else:
        fake_transactions["buy_plan_id"].append( np.random.choice(df_fake_plans.index.tolist()) )
        fake_transactions["country"].append( np.random.choice(list(avl_countries.keys()), p=p_countries) )
        new_subs["sub_id"].append( j )
        new_subs["full_name"].append(fake.name())
        new_subs["created_at"].append(fake_transactions["created_at"][i])
        new_subs["country"].append(fake_transactions["country"][i])
        new_subs["phone_no"].append('+' + str(avl_countries[fake_transactions["country"][i]]) + ' '  + str(random.randint(190,499)) + ' ' + str(random.randint(100,999)) + ' ' + str(random.randint(1000,9999)))
        new_subs["cur_plan_id"].append(fake_transactions["buy_plan_id"][i])
        fake_transactions["sub_id"].append( j )
        j += 1
df_fake_transactions = pd.DataFrame(fake_transactions)
df_fake_subscribers = df_fake_subscribers.append(pd.DataFrame(new_subs),ignore_index=True)


#USAGE
""" Generate actions to populate usage table """
avl_actions = Const.ACTIONS
p_actions = Const.p_actions
for i in range(Const.USE_RANGE):
    fake_usage_data["usage_id"].append( i )
    fake_usage_data["sub_id"].append( np.random.choice(df_fake_subscribers["sub_id"].tolist()) )
    fake_usage_data["use_type"].append( np.random.choice(avl_actions,p=p_actions) )
    fake_usage_data["usage_time"].append( fake.date_time_between(start_date='-2y', end_date='now') )
    fake_usage_data["amount"].append( random.randint(1,60) )
    fake_usage_data["is_fraud"].append( False )
df_fake_usage_data = pd.DataFrame(fake_usage_data)


#TRACKING
def comparePlans(t_id):
    sub_affected = df_fake_transactions.iloc[t_id,1]
    init_plan_id = df_fake_subscribers.loc[sub_affected,"cur_plan_id"]
    changed_plan_id = df_fake_transactions.loc[t_id,"buy_plan_id"]
    df_fake_subscribers.at[sub_affected,"cur_plan_id"] = changed_plan_id
    return df_fake_plans.iloc[changed_plan_id,3] - df_fake_plans.iloc[init_plan_id,3]

def track_change(t_id):
    """ Keeps track of plan changes """
    cmp = comparePlans(t_id)
    if cmp == 0:
        return
    fake_tracking["tracking_id"].append( track_change.count )
    fake_tracking["trans_id"].append( t_id )
    fake_tracking["upgrade"].append( bool(cmp>0) )
    fake_tracking["cost_diff"].append( cmp )
    track_change.count += 1
track_change.count = 0

for i in tracklist:
    track_change(i)
df_fake_tracking = pd.DataFrame(fake_tracking)




tables = Const.TABLES
data_frames = [df_fake_plans, df_fake_subscribers, df_fake_features, df_fake_tracking, df_fake_transactions, df_fake_usage_data]
data = dict(zip(tables,data_frames))
params = Const.PARAMS
pg_connection = psycopg2.connect(dbname=params["NAME"], user=params["USER"], password=params["PASSWORD"], host=params["HOST"], port=params["PORT"])


def execute_values(pg_conn, df, table):
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ','.join(list(df.columns))
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    db_cursor = pg_conn.cursor()
    try:
        extras.execute_values(db_cursor, query, tuples)
        pg_conn.commit()
        print("Data inserted into {} successfully...".format(table))
    except(Exception, psycopg2.DatabaseError) as err:
        print(err)
        pg_conn.rollback()
        db_cursor.close()


for table in tables:
    execute_values(pg_connection, data[table], table)

print("Insert Success")
pg_connection.close()