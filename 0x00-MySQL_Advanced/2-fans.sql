-- calculate band fans
WITH FanCounts AS (
  SELECT origin, SUM(nb_fans) AS total_fans
  FROM metal_bands
  GROUP BY origin
)
SELECT origin, total_fans, DENSE_RANK() OVER (ORDER BY total_fans DESC) AS country_rank
FROM FanCounts
ORDER BY total_fans DESC;
