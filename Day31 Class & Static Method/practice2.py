from practice1 import Employee

# ==========================================
# TESTING SECTION
# ==========================================

# Test Case 1: Normal employee
emp1 = Employee(101, "Rahul", 40000)
emp1.salary_payslip()

# Test Case 2: High salary employee
emp2 = Employee(102, "Sneha", 90000)
emp2.salary_payslip()

# Test Case 3: Zero salary (edge case)
emp3 = Employee(103, "Test", 0)
emp3.salary_payslip()