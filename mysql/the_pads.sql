SELECT CONCAT(Name, "(", LEFT(Occupation, 1),")" ) as Names
FROM OCCUPATIONS
ORDER BY Names ASC;

SELECT CONCAT("There are a total of ", COUNT(Occupation), " ",  LOWER(Occupation),"s.") as asd
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Occupation) ASC;