SELECT
  people.id         AS id,
  people.name       AS name,
  COUNT(toys.name)  AS toy_count
FROM
  people
JOIN
  toys
ON
  people.id = toys.people_id
GROUP BY
  people.id
;
