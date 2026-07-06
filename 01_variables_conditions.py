# #TOPIC : Variables & conditonal statements

# #Q1: Create variables to store your name, age, and city, then print them
# name="Saloni"
# age=21
# city="Gwalior"
# print("Name:",name)
# print("Age:",age)
# print("City:",city)

# #Q2: Take two numbers and check which one is greater
# a=78
# b=96
# if a>b:
#     print(a,"is greater")
# elif b>a:
#     print(b,"is greater")
# else:
#     print("both numbers are equal")

# #Q3:
# # Check whether a number is positive,negative or zero
# num=int(input("enter number"))
# if num>0:
#     print("the number is positive")
# elif num<0:
#     print("the number is negative")
# else:
#     print("the number is zero")  

# #Q4: Check whether a number is even or odd
# num=int(input("enter your number"))
# if num%2==0:
#     print(num,"is even")
# else:
#     print(num,"is odd")  


# #Q5: Check whether  a person is eligible to vote(age>=18)
# age=int(input("enter your age"))
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")    

# #Q6: Grade a student based on marks(1-100)
# marks=int(input("enter your marks"))
# if marks>=90:
#     grade="A"
# elif marks>=75:
#     grade="B"
# elif marks>=60:
#     grade="C"
# else:
#     grade="D"

# print("Grade",grade)

# #Q7:Check if a number is divisible by both 3 and 5
# n=int(input("enter number"))
# if n%3==0 and n%5==0:
#     print(n,"is divisible by both 3 and 5")
# else:
#     print(n,"is not divisible by both 3 and 5")     

#Q8: Find the largest of three numbers
# x=45
# y=78
# z=96

# if x>y and x>z:
#     largest=x
# elif y>z and y>x:
#     largest=y
# else:
#     largest=z

# print("largest:",largest)

# #Q9: Check the data type of a variable using type()
# value=45.2
# print("data type of value is:",type(value))

# #Q10: Take a variable storing salary and check bonus eligibility (salary<50000)
# salary=int(input("enter your salary"))

# if salary <50000:
#     print("eligible for bonus")
# else:
#     print("not eligible for bonus")    

#=============================================================================#
#ADVANCED QUESTIONS

#Q11: Check if a year is a leap year 
# year=int(input("enter year"))
# if (year%4==0 and year%100!=0) or (year%400==0):
# #     print(year,"is a leap year")
# # else:
# #     print(year,"is not a leap year")     


# #Q12: Categorize BMI (Body Mass Index)
# weight=45  #in kg
# height=1.5  #in meters

# bmi=weight/(height**2)

# if bmi<18.5:
#     category="underweight"
# elif bmi<25:
#     category="normal" 
# elif bmi<30:
#     category="overweight"
# else:
#     category="obese"

# print("category:",category)


# #Q13: Check if a triable is valid based on three angles(sum=180)
# angle1=60
# angle2=70
# angle3=50

# if angle1+angle2+angle3==180:
#     if angle1==angle2==angle3:
#         print("valid traingle-equlateral")
#     elif angle1==angle2 or angle2==angle3 or angle1==angle3:
#         print("valid traingle-isosceles")
#     else:
#         print("valid traingle-scalene")
# else:
#     print("not a valid traingle")       


#Q14: Determine electricity bill based on units consumed(slab system)

# units=250
# if units<=100:
#     bill=units*3
# elif units<=200:
#     bill=(100*3)+(units-100)*5
# else:
#     bill=(100*3)+(100*5)+(units-200)*8

# print("electricity bills: Rs.",bill) 


# #15: Check password strength based on multiple conditions
# password=input("enter your password")
# has_upper=any(char.isupper() for char in password)
# has_lower=any(char.islower()for char in password)
# has_digit=any(char.isdigit()for char in password)
# has_special=any(char in "!@#$%^&*" for char in password)
# is_long_enough=len(password)>=8

# if has_upper and has_lower and has_digit and has_special and is_long_enough:
#     print("strong password")
# elif is_long_enough and (has_upper or has_lower) and has_digit:
#     print("moderate password")
# else:
#     print("weak password")    


#Q16: Determine ticket price based on age and day(weekday/weekend)
# age=int(input("enter your age"))
# day_type=input("enter which day weekend or weekday")
# if age<5:
#     price=0
# elif age<12:
#     price=100 if  day_type=="weekday" else 150
# elif age<60:
#     price=200 if day_type=="weekday" else 250
# else:
#     price=100 if day_type=="weekday" else 130  

# print("ticket price Rs", price)    

#Q17: Check divisibility rules combined(fizzbuzz logic)
# num=int(input("enter number"))
# if num%3==0 and num%5==0:
#     print("fizzbuzz")
# elif num%3==0:
#     print("fizz")
# elif num%5==0:
#     print("buzz")
# else:
#     print(num)


#Q18: Loan eligibility check based on income and credit score income
# loan_amt=int(input("enter loan amt"))
# income=int(input("enter income"))
# credit_score=int(input("enter credit score"))
# if income>=30000 and credit_score>=700:
#     print("loan approved,full amount",loan_amt)
# elif income>=20000 and credit_score>=650:
#     print("loan approved, partial amount",loan_amt/2)
# else:
#     print("loan rejected , low income and credit score")


# #Q19:Classify a triangle as right angled using pythagoras theorem
# side_a=5
# side_b=4
# side_c=3

# sides=sorted([side_a,side_b,side_c])
# if sides[0]**2+sides[1]**2==sides[2]**2:
#     print("right angle traingle")
# else:
#     print("not a right angled traingle")  


#Q20: Employee performance rating based on multiple KPIs
# attendance=92       #percentage
# sales_target=105     #percentage
# customer_rating=4.5     #out of 5

# if attendance>=90 and sales_target>=100 and customer_rating>=4:
#     print("excellent")
# elif attendance>=80 and sales_target>=80 and customer_rating>=3:
#     print("good")
# elif attendance>=70 and sales_target>=60:
#     print("average")
# else:
#     print("needs improvemnt")            

 

             