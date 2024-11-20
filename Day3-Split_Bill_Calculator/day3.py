bill = int(input("Enter total bill in RS : "))
tip = int(input("Enter tip in % eg 10, 12, 15 :"))
total = tip/100 * bill + bill
split = int(input("How many people to split the bill : "))
final = total / split
print(f"Your split bill is {final} per head.")