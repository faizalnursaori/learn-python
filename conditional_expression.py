# Ini bisa disebut juga ternary operator

# If-Else
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Ternary
number = 3
result = "Even" if number % 2 == 0 else "Odd"
print(result)

user_role = "admin"
access = "Full Access" if user_role == "admin" else "Limited Access"
print(access)