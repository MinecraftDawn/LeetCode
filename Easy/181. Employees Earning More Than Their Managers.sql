# Write your MySQL query statement below
SELECT E.Name as Employee
FROM Employee AS E, Employee AS M
WHERE E.ManagerId = M.Id AND E.Salary > M.Salary;