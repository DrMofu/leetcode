SELECT Users.user_id AS "buyer_id", Users.join_date AS "join_date", IFNULL(buy_info.orders_in_2019,0) AS orders_in_2019 
FROM Users
LEFT JOIN
(
    SELECT buyer_id,count(1) as "orders_in_2019" 
    FROM Orders 
    WHERE order_date LIKE "2019%" GROUP BY buyer_id
) AS buy_info
ON Users.user_id=buy_info.buyer_id
;
