-- The Script implements a subquerry
-- The Script lists all cities of carlifornia
SELECT `id`
FROM `cities`
WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name` = 'California')
ORDER BY `id`;
