SELECT 
  race     AS race
  COUNT(*) AS count
FROM 
  demographics
GROUP BY 
  race
ORDER BY 
  count DESC
;
