person = {"name": "Alice", "age": 30, "city": "New York"}

# another way to create a dictionary
scores = dict(math=95, english=87, science=92)

print(person)

# data retrieval
print(person["name"])
print(person["age"])
print(person["city"])

# data manipulation
person["name"] = "David"
person["age"] = 24
person["city"] = "SF"
person["license"] = True

print(person)

del person["age"]
print(person)
