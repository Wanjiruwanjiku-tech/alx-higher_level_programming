-- The script lists all records
-- Where the score is >= 10
SELECT `score`, `name`
FROM `second_table`
WHERE `id` >= 10
ORDER BY `score` DESC;
