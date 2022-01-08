ALTER TABLE plans ADD FOREIGN KEY (feature_id) REFERENCES features (feature_id);
ALTER TABLE usage_data ADD FOREIGN KEY (sub_id) REFERENCES subscribers (sub_id);
ALTER TABLE transactions ADD FOREIGN KEY (sub_id) REFERENCES subscribers (sub_id);
ALTER TABLE subscribers ADD FOREIGN KEY (cur_plan_id) REFERENCES plans (plan_id);
ALTER TABLE transactions ADD FOREIGN  KEY (buy_plan_id) REFERENCES plans (plan_id);
ALTER TABLE tracking ADD FOREIGN KEY (trans_id) REFERENCES transactions (trans_id);
