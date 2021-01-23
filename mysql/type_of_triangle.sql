SELECT (
    IF (A = B AND B = C AND A = C, "Equilateral", 
        IF (A + B <= C, "Not A Triangle", 
            IF (A = B OR B = C OR A = C, "Isosceles", "Scalene")))
    )
FROM TRIANGLES