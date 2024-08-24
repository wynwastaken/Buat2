print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:\n")
bill = 0
if size == "S":
    #print("Your pizza size small")
    bill += 15
    topping1 = input("want to add pepperoni(Y/N) ?:\n")
    if topping1 == "Y":
        bill += 2
elif size == "M":
    #print("Your pizza size medium")
    bill += 20
    topping1 = input("want to add pepperoni(Y/N) ?:\n")
    if topping1 == "Y":
        bill += 3

else:
    #print("Your pizza size large")
    bill += 25
    topping1 = input("want to add pepperoni(Y/N) ?:\n")
    if topping1 == "Y":
        bill += 3

topping2 = input("Do you want to add extra cheese(Y/N) ?:\n")
if topping2 == "Y":
    bill += 1
    print(f"Your final bill is: ${bill}.")
else:
    print(f"Your final bill is: ${bill}.")
