hours_worked = float(input("Enter the total number of hours worked this week: "))
hourly_wage = float(input("Enter the pay per standard hour: "))
standard_hours = 44
over_standard_hours = max(0, hours_worked - standard_hours)
net_pay = standard_hours * hourly_wage + over_standard_hours * hourly_wage * 1.5
print(f"The employee's actual earnings: {net_pay}")