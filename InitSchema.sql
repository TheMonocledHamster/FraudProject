CREATE TABLE subscribers (
  sub_id SERIAL PRIMARY KEY,
  full_name varchar,
  created_at timestamp,
  country_code int,
  phone_no int,
  cur_plan_id int
);

CREATE TABLE transactions (
  trans_id SERIAL PRIMARY KEY,
  sub_id int,
  trans_type varchar,
  created_at timestamp,
  trans_location varchar,
  buy_plan_id int
);

CREATE TABLE plan (
  plan_id int PRIMARY KEY,
  plan_cost int,
  validity int,
  plan_data numeric,
  feature_id int,
  Postpaid boolean
);

CREATE TABLE usage_data (
  usage_id SERIAL PRIMARY KEY,
  sub_id int,
  use_type varchar,
  usage_time timestamp,
  amount int
);

CREATE TABLE features (
  feature_id int PRIMARY KEY,
  sms int,
  netflix boolean,
  prime boolean,
  hotstar boolean
);

ALTER TABLE plan ADD FOREIGN KEY (feature_id) REFERENCES features (feature_id);

ALTER TABLE usage_data ADD FOREIGN KEY (sub_id) REFERENCES subscribers (sub_id);

ALTER TABLE transactions ADD FOREIGN KEY (sub_id) REFERENCES subscribers (sub_id);

ALTER TABLE subscribers ADD FOREIGN KEY (cur_plan_id) REFERENCES plan (plan_id);

ALTER TABLE transactions ADD FOREIGN  KEY (buy_plan_id) REFERENCES plan (plan_id);