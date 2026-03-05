# program that will determine the monthly contribution someone will pay from  the gross salary 
grossIncome = int(input("Enter grossIncome"))
#print the monthly income 

if grossIncome > 0 and grossIncome <= 5999 :
    print("Monthly Contribution", float(150.00))

elif grossIncome >= 6000 and grossIncome <=7999 : 
    print("Monthly contribution", float(300.00))

elif grossIncome >= 8000 and grossIncome <=11999 : 
    print("Monthly contribution", float(400.00))

elif grossIncome >= 12000 and grossIncome <=14999:  
    print("Monthly contribution", float(500.00))

elif grossIncome >= 15000 and grossIncome <=19999: 
    print("Monthly contribution", float(600.00))

elif grossIncome >= 20000 and grossIncome <=24999: 
    print("Monthly contribution", float(750.00))

elif grossIncome >= 25000 and grossIncome <=29999: 
    print("Monthly contribution", float(850.00))

elif grossIncome >= 30000 and grossIncome <=49999: 
    print("Monthly contribution", float(1000.00))

elif grossIncome >= 50000 and grossIncome <=99999:
    print("Monthly contribution", float(1500.00))

elif grossIncome < 0 :
    print("monthly Conribution Invalid")

else :
    print("Monthly Contribution", float(2000.00))




