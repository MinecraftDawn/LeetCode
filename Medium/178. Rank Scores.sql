# Write your MySQL query statement below
SELECT s1.Score, COUNT(DISTINCT s2.Score) AS Rank
FROM Scores AS s1, Scores AS s2
WHERE s2.Score >= s1.Score
GROUP BY s1.Id
ORDER BY Rank;