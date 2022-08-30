-- SELECT直接显示
SELECT 
(
    SELECT DISTINCT salary FROM Employee 
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;