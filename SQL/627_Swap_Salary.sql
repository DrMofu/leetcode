UPDATE salary 
SET sex = CASE sex WHEN "m" THEN "f" ELSE "m" END;
-- SET sex = CASE WHEN sex="m" THEN "f" ELSE "m" END;