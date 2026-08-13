message = "I am learning python for ai"

print("Python" in message) #false because in actual string, it is python not Python
print(message.startswith("I"))
print(message.endswith("ai"))

print(message.find("python")) #this is also case sensitive
print(message.count("a"))

new_message = message.replace("Python", "Rust")
print(new_message)