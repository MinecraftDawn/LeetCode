# Write your MySQL query statement below
SELECT C.Name AS Customers
FROM Customers AS C
WHERE C.Id NOT IN (SELECT O.CustomerId
                  FROM Orders AS O);