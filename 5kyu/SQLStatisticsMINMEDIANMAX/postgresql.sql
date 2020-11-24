SELECT
  MIN(score)                          AS min,
  percentile_cont(0.5) WITHIN GROUP (
    ORDER BY
      score
    )                                 AS median,
  MAX(score)                          AS max
FROM
  result
;
