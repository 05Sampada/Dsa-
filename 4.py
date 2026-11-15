def employee_details(emp_id, empname, empqualification,
                     empdesignation, empsalary, emp_currentmonthrank):

    print("Employee ID:", emp_id)
    print("Employee Name:", empname)
    print("Qualification:", empqualification)
    print("Designation:", empdesignation)

    if emp_currentmonthrank > 4:
        empsalary = empsalary + 2500
        print("Incentive: Rs.2500")
    else:
        print("Incentive: Rs.0")

    print("Final Salary: Rs.", empsalary)


# Calling the function
employee_details(101, "Asha", "MCA", "Manager", 30000, 5)