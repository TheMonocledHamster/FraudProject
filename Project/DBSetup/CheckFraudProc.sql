CREATE OR REPLACE PROCEDURE check_fraud()
LANGUAGE PLPGSQL
AS $$
BEGIN
	UPDATE usage_data
	SET is_fraud = True
	WHERE amount > 100;
	COMMIT;
END; $$