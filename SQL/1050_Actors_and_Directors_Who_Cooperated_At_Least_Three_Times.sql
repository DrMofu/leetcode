-- SELECT actor_id, director_id FROM ActorDirector GROUP BY actor_id, director_id HAVING COUNT(actor_id)>=3;
-- SELECT actor_id, director_id FROM ActorDirector GROUP BY actor_id, director_id HAVING COUNT(director_id)>=3;
-- SELECT actor_id, director_id FROM ActorDirector GROUP BY actor_id, director_id HAVING COUNT(*)>=3;
SELECT actor_id, director_id FROM ActorDirector GROUP BY actor_id, director_id HAVING COUNT(1)>=3;