CREATE OR REPLACE VIEW frauds AS
SELECT s.sub_id,s.full_name,s.country AS home_country,phone_no,s.country AS fraud_locale 
FROM subscribers s
JOIN usage_data u ON s.sub_id = u.sub_id
WHERE u.is_fraud
UNION
SELECT s.sub_id,s.full_name,s.country AS home_country,phone_no,t.country AS fraud_locale 
FROM subscribers s
JOIN transactions t ON s.sub_id = t.sub_id
WHERE t.is_fraud;