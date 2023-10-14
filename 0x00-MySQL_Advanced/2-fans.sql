-- calculate band fans
SELECT origin, total_fans,
       DENSE_RANK() OVER (ORDER BY total_fans DESC) AS country_rank
FROM (
  SELECT origin, SUM(nb_fans) AS total_fans
  FROM metal_bands
  GROUP BY origin
) AS FanCounts
ORDER BY country_rank;
