# Write your MySQL query statement below
SELECT D.Name AS Department , E.Name AS Employee, E.Salary
FROM Employee AS E
INNER JOIN Department AS D ON E.DepartmentId = D.Id
WHERE e.Salary = (SELECT MAX(E2.Salary)
                 FROM Employee AS E2
                 WHERE E2.DepartmentId = D.Id);