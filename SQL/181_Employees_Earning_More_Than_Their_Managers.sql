-- 创建子表比JOIN开销更大，不建议使用
-- SELECT name AS "Employee" FROM employee e
-- WHERE salary > 
-- (
--     SELECT salary FROM employee where id=e.managerID
-- );


SELECT
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id AND a.Salary > b.Salary
;


SELECT
     a.NAME AS Employee
FROM Employee AS a JOIN Employee AS b
     ON a.ManagerId = b.Id
     AND a.Salary > b.Salary
;