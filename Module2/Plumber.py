""" assignemnt: Chapter2 VAT
    created on 1 nov. 2019
    author: Gaia Liistro """

hourly_wages = float(raw_input("Enter the hourly wages: "))
hours_worked = int(round(float(raw_input("Enter the number of hours worked: "))))
CALL_OUT_COST = 16.00 #euros
repair_cost = float(hourly_wages * hours_worked + CALL_OUT_COST)

print "the total cost of the repair is %.2f euros" %(repair_cost)