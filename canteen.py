#a program for meal deductions according to employees wage range
salary = int(input("current salary:"))
if salary >=30000 and salary <= 100000:
    print(salary - 3000)
elif salary >= 101000 and salary <= 200000:
    print(salary -2500)
elif salary >= 201000 and salary <= 300000:
    print(salary - 2000)
else:
    print(salary)