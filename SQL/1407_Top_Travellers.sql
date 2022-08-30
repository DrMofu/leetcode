SELECT Users.name, IFNULL(dis_records.travelled_distance,0) AS "travelled_distance"
FROM Users
LEFT JOIN
(
    SELECT user_id, SUM(distance) AS travelled_distance FROM Rides GROUP BY user_id
) AS dis_records
ON Users.id = dis_records.user_id
ORDER BY dis_records.travelled_distance DESC, Users.name;