from faker import Faker
from numpy import NaN
import pandas as pd
from collections import defaultdict
import random

fake = Faker()
fake_data = defaultdict(list)

for _ in range(5):
    fake_data["full_name"].append( fake.name() )
    fake_data["created_at"].append( None )
    fake_data["country_code"].append( random.randint(1,999) )
    fake_data["phone_number"].append( random.randint(1000000000,9999999999) )
    fake_data["cur_plan_id"].append( None )

df_fake_data = pd.DataFrame(fake_data)

print(df_fake_data)