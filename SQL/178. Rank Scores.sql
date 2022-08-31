-- SELECT scores.score, sorted.rank FROM scores
-- LEFT JOIN
-- (
--     SELECT first.score, COUNT(first.score) as "rank" FROM 
--     (SELECT DISTINCT score FROM scores) AS first,
--     (SELECT DISTINCT score FROM scores) AS second
--     WHERE first.score<=second.score GROUP BY first.score
-- )AS sorted
-- ON scores.score = sorted.score
-- ORDER BY scores.score DESC;

SELECT
  Score,
  (SELECT count(distinct Score) FROM Scores WHERE Score >= s.Score) AS "Rank"
FROM Scores s
ORDER BY Score desc


SELECT
  Score,
  (SELECT count(*) FROM (SELECT distinct Score s FROM Scores) tmp WHERE s >= Score) AS "Rank"
FROM Scores
ORDER BY Score desc