select department.name as "Department", employee.name as "Employee", employee.salary as "Salary" from employee,
department,
(
    select departmentid,max(salary) as salary from employee group by departmentid
) max_salary
where employee.salary=max_salary.salary and  employee.departmentId=max_salary.departmentid and department.id = employee.departmentId;