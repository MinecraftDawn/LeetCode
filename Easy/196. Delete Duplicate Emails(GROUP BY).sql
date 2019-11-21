# Write your MySQL query statement below
DELETE P1
FROM Person AS P1
WHERE P1.Id NOT IN(
    SELECT *
    FROM(
        SELECT MIN(P2.Id)
        FROM Person AS P2
        GROUP BY P2.Email) AS TMP);