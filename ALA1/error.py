print("Interest Calculator")
years = int(input("Enter years: "))
principal = 1000
rate = 5
i = 1
total_interest = 0
while i <= years:
interest = principal * rate * i / 100
total_interest = total_interest + interest
print("Year", i, "Interest:", interest)
if interest > 200
print("High interest")
else:
print("Normal interest")
i = i + 1
print("Total Interest:", total_interest
if total_interest > 1000:
print("Good return")
else:
print("Low return")
