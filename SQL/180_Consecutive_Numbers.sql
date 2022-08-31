-- SELECT DISTINCT log1.num AS "ConsecutiveNums" FROM
-- logs log1,
-- logs log2,
-- logs log3
-- WHERE log1.num = log2.num AND log2.num=log3.num 
-- AND log1.id=log2.id-1 AND log2.id=log3.id-1;


select distinct Num as ConsecutiveNums
from Logs
where (Id + 1, Num) in (select * from Logs) and (Id + 2, Num) in (select * from Logs);