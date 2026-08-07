"""
57) Employee Payroll System
----------------------------
Class Employee with attributes: emp_id, name, basic_salary
 
Requirements:
- Constructor should initialize the attributes.
- Method calculate_allowances() -> HRA = 20% of salary, DA = 10% of salary.
- Method calculate_gross_salary() -> Basic + HRA + DA.
- Method calculate_net_salary() -> Gross - Tax (10% of gross).
- Method display_payslip() -> Show employee details and full salary calculation.
"""

class Employee:
    da = 10   # - 10%
    hra = 20  # - 20%
    tax = 10  # - 10%

    def __init__(self,id,nm,bs):
        # instance attribute 
        self.emp_id = id 
        self.name = nm
        self.basic_salary = bs

    def calculate_allowance(self):
        HRA_AMOUNT = self.basic_salary*Employee.hra/100
        DA_AMOUNT = self.basic_salary*Employee.da/100
        return HRA_AMOUNT,DA_AMOUNT

    def calculate_gross_salary(self):
        HRA_AMOUNT,DA_AMOUNT = self.calculate_allowance()
        gs = self.basic_salary + HRA_AMOUNT + DA_AMOUNT
        return gs

    def calculate_net_salary(self):
        gs = self.calculate_gross_salary()
        tax_amount = gs*Employee.tax/100
        ns = gs-tax_amount
        return ns 

    def salary_payslip(self):
        hra,da = self.calculate_allowance()
        gs =self.calculate_gross_salary()
        ns = self.calculate_net_salary()

        salary_slip = f'''
        ------------------------------------
              EMPLOYEE PAYSLIP
        ------------------------------------
        Emp_ID : {self.emp_id}
        Emp_Name : {self.name}
        HRA Amount : {hra}
        DA Amount : {da}
        Gross Salary : {gs}
        Net Salary : {ns}

        '''
        print(salary_slip)

