DROP TRIGGER IF EXISTS detect_fraud_trans ON transactions;
CREATE TRIGGER detect_fraud_trans
AFTER INSERT
ON transactions
FOR EACH ROW
EXECUTE PROCEDURE detect_fraud_trans_fn();