CREATE TABLE subscribers (
  sub_id int primary key,
  full_name varchar,
  created_at timestamp,
  country varchar,
  phone_no int,
  cur_plan_id int
);

CREATE TABLE transactions (
  trans_id int primary key,
  sub_id int,
  trans_type varchar,
  created_at timestamp,
  country varchar,
  buy_plan_id int
);

CREATE TABLE plan (
  plan_id int primary key,
  plan_data numeric,
  validity int,
  plan_cost int,
  feature_id int,
  postpaid boolean
);

CREATE TABLE usage_data (
  usage_id int primary key,
  sub_id int,
  use_type varchar,
  usage_time timestamp,
  amount int
);

CREATE TABLE features (
  feature_id int primary key,
  sms int,
  netflix boolean,
  primevideo boolean,
  hotstar boolean
);

ALTER TABLE plan ADD FOREIGN KEY (feature_id) REFERENCES features (feature_id);

ALTER TABLE usage_data ADD FOREIGN KEY (sub_id) REFERENCES subscribers (sub_id);

ALTER TABLE transactions ADD FOREIGN KEY (sub_id) REFERENCES subscribers (sub_id);

ALTER TABLE subscribers ADD FOREIGN KEY (cur_plan_id) REFERENCES plan (plan_id);

ALTER TABLE transactions ADD FOREIGN  KEY (buy_plan_id) REFERENCES plan (plan_id);
