CREATE OR REPLACE FUNCTION track_plans_fn()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE 
    new_cost INTEGER;
    old_cost INTEGER;
    track_id INTEGER;
BEGIN
    SELECT plans.plan_cost INTO new_cost
    FROM plans
    WHERE plan_id = NEW.buy_plan_id;

    SELECT plans.plan_cost INTO old_cost
    FROM plans
    JOIN subscribers ON subscribers.cur_plan_id = plans.plan_id
    WHERE subscribers.sub_id = NEW.sub_id;

    SELECT MAX(tracking_id)+1 INTO track_id
    FROM tracking;

    INSERT INTO tracking(tracking_id, trans_id, upgrade, cost_diff)
    VALUES (track_id, NEW.trans_id, (new_cost-old_cost>0), (new_cost-old_cost));
	
	UPDATE subscribers
	SET cur_plan_id = NEW.buy_plan_id 
	WHERE sub_id = NEW.sub_id;
	
	RETURN NEW;
END; 
$$
