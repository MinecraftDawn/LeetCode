# Write your MySQL query statement below
SELECT DISTINCT T1.Num as ConsecutiveNums
FROM Logs AS T1
LEFT JOIN Logs AS T2
    ON T1.Id = T2.Id-1
LEFT JOIN Logs AS T3
    ON T1.Id = T3.Id-2
WHERE T1.Num = T2.Num AND T1.Num = T3.Num;