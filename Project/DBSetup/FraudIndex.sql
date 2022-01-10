DROP INDEX IF EXISTS fraud_idx;
CREATE INDEX fraud_idx
ON usage_data(is_fraud);