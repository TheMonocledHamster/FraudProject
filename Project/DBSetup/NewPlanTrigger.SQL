DROP TRIGGER IF EXISTS call_track_plans ON transactions;
CREATE TRIGGER call_track_plans
AFTER INSERT
ON transactions
FOR EACH ROW
WHEN (UPPER(NEW.trans_type) = 'NEW PLAN')
EXECUTE PROCEDURE track_plans_fn();
