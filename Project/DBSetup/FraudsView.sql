CREATE OR REPLACE VIEW frauds AS
SELECT DISTINCT s.sub_id,s.full_name,s.country AS home_country,phone_no,t.country AS fraud_locale 
FROM subscribers s
INNER JOIN usage_data u ON s.sub_id = u.sub_id
INNER JOIN transactions t ON t.sub_id = s.sub_id
WHERE t.is_fraud OR u.is_fraud;