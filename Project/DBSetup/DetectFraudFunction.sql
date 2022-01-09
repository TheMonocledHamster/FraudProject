CREATE OR REPLACE FUNCTION detect_fraud_trans_fn()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
	IF UPPER(NEW.country) != subscribers.country WHERE subscribers.sub_id=NEW.sub_id AND UPPER(NEW.trans_type)=UPPER('SIM Change') THEN
	    NEW.is_fraud := (1-1=0);
	END IF;
	RETURN NEW;
END; 
$$