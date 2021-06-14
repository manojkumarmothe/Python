# Expense Calculator

from tabulate import *
from user_defined_exception import *

def expense_calc(salary,expenditure_data,temp_salary):
    expense_calc=[]
    expense_calc.append(['salary',salary])
    for expenditure_name,expenditure_amount in expenditure_data.items():
        expense_calc.append([expenditure_name,expenditure_amount])
    else:
        expense_calc.append(['total',sum(expenditure_data.values())])
        expense_calc.append(['balance',temp_salary])
    print (tabulate(expense_calc))

try:
    salary=input("Enter Salary :").strip()
    invalid_input_count = 0
    temp_str_salary=salary.replace(".","") 
    while not(temp_str_salary.isdecimal()) or salary=="0":
        invalid_input_count  += 1
        if invalid_input_count<5:
            salary=input("Please Enter Valid Input:").strip()
            temp_str_salary=salary.replace(".","")
        else:
            raise InvalidInputException("You have entered incorrect salry 5 times")

    expenditure_data={}
    temp_salary=float(salary)  

    while True:
        print("Select Options:\n1:Expenditure\nq:Quit")
        option=input("Enter Option :").strip()

        if option=="1":
            exp_name=input("Enter Expenditure name :").strip()
   
            exp_amount=input(f"Enter the amount for {exp_name}:")
            temp_exp_amount=exp_amount.replace(".","")
            while temp_exp_amount.isdecimal()!= True:
                print("Please Enter Valid Amount")
                exp_amount=input(f"Enter Expenditure {exp_name}:")
                temp_exp_amount=exp_amount.replace(".","")

            exp_amount = float(exp_amount)
            
            if exp_amount > temp_salary:
                raise InsufficientFunds("Insufficient funds")

            if exp_name not in expenditure_data:
                expenditure_data[exp_name]= exp_amount
            else:
                expenditure_data[exp_name]= expenditure_data[exp_name]+exp_amount
            temp_salary -= exp_amount

        elif option=="q":
            break
        else:
            print("You have entered wrong input")
                 
except InvalidInputException as msg:
    print(msg)

except InsufficientFunds as msg:
    print(msg)
    expense_calc(salary,expenditure_data,temp_salary)
else:
    expense_calc(salary,expenditure_data,temp_salary)
finally:
    print("Thank you")











              




