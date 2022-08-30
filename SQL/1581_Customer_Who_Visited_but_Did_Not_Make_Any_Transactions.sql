SELECT join_table.customer_id AS "customer_id", COUNT(1) AS "count_no_trans" FROM
(
    SELECT Visits.visit_id,Visits.customer_id,Transactions.transaction_id FROM Visits
    LEFT JOIN Transactions
    ON Visits.visit_id=Transactions.visit_id
) AS join_table 
WHERE join_table.transaction_id is NULL
GROUP BY join_table.customer_id
;