temperature = 25

if temperature > 25:
    print("it's hot!")
elif temperature == 25:
    print("it's pleasant")
else:
    print("it's cold!")


has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Allowed to watch the movie.")
    else:
        print("Needs supervision.")

else:
    print("Please buy a ticket!")
