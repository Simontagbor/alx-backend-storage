-- filter based on band style
SELECT band_name, 
       (CASE 
         WHEN split = 0 THEN (2022 - formed)
         ELSE (split - formed)
       END) AS lifespan
FROM metal_bands
WHERE band_style = 'Glam rock'
ORDER BY lifespan;

