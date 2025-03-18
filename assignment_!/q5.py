service_year=(int(input("enter your service year 4")))
current_salary=(float(input("enter your salary : ")))
if service_year>=5:
    bonus= current_salary * 0.05
    print("your got a bonus of :" ,bonus)
else:
    print("sorry no bonus as you service of years is less than 5 years")
