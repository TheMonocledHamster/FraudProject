CREATE TABLE IF NOT EXISTS subscribers (
  sub_id int primary key,
  full_name varchar,
  created_at timestamp,
  country varchar,
  phone_no varchar,
  cur_plan_id int
);

CREATE TABLE IF NOT EXISTS transactions (
  trans_id int primary key,
  sub_id int,
  trans_type varchar,
  created_at timestamp,
  country varchar,
  buy_plan_id int,
  is_fraud boolean
);

CREATE TABLE IF NOT EXISTS plans (
  plan_id int primary key,
  plan_data numeric,
  validity int,
  plan_cost int,
  feature_id int,
  postpaid boolean
);

CREATE TABLE IF NOT EXISTS usage_data (
  usage_id int primary key,
  sub_id int,
  use_type varchar,
  usage_time timestamp,
  amount int,
  is_fraud boolean 
);

CREATE TABLE IF NOT EXISTS features (
  feature_id int primary key,
  sms int,
  netflix boolean,
  primevideo boolean,
  hotstar boolean
);

CREATE TABLE IF NOT EXISTS tracking (
  tracking_id int primary key,
  trans_id int,
  upgrade boolean,
  cost_diff float
);
