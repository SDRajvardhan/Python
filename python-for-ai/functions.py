# static
def greet():
    print("Hello World!")


greet()


# static
def check_weather():
    temperature = 18
    if temperature > 25:
        print("hot")
    else:
        print("normal")


check_weather()


# dynamic
def greet(firstname, lastname):
    print(f"Hello, {firstname} {lastname}!")


greet("Rajvardhan", "Singh")


# dynamic
def check_weather(temperature):
    if temperature > 25:
        print("hot")
    else:
        print("normal")


check_weather(26)
