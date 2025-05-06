-- table A: entry_date, entry_time, value
-- filter table A to get AVG based on entry_date
-- with that AVG, filter the value to have greater or equal value 

SELECT m1.entry_date, m1.entry_time, m1.value
FROM measurements as m1
JOIN (
    SELECT entry_date, AVG(value) as avg_val
    FROM measurements
    GROUP BY entry_date
) m2 ON m1.entry_date = m2.entry_date
WHERE m1.value >= m2.avg_val

