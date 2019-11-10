# Write your MySQL query statement below
SELECT D.Name AS Department, E.Name AS Employee, E.Salary
FROM Employee AS E
INNER JOIN Department AS D ON E.DepartmentId = D.Id
WHERE (SELECT COUNT(DISTINCT E2.Salary)
       FROM Employee AS E2
       WHERE E.DepartmentId = E2.DepartmentId AND E2.Salary > E.Salary) < 3;