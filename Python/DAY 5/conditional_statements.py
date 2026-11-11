# 1. if
print("--- 1. if ---")
age = 20
if age >= 18:
    print("You can vote")

# 2. if-else
print("\n--- 2. if-else ---")
n = 7
if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")

# 3. if-elif-else (grades)
print("\n--- 3. if-elif-else ---")
marks = 72
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# Positive / negative / zero
num = -5
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 4. Nested if
print("\n--- 4. Nested if ---")
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Bring your ID")
else:
    print("Under age")

# 5. Ternary
print("\n--- 5. Ternary ---")
x = 10
print("Even" if x % 2 == 0 else "Odd")

# 6. Logical operators: leap year
print("\n--- 6. Leap year ---")
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# 7. Largest of three numbers
print("\n--- 7. Largest of three ---")
a, b, c = 15, 42, 27
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# 8. Membership operator: vowel check
print("\n--- 8. Vowel or consonant ---")
ch = "e"
if ch.lower() in "aeiou":
    print(ch, "is a vowel")
else:
    print(ch, "is a consonant")

# 9. Truthy / falsy
print("\n--- 9. Truthy / falsy ---")
name = ""
if name:
    print("Hello,", name)
else:
    print("Name is empty")

# 10. Login check
print("\n--- 10. Login check ---")
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# 11. match-case (Python 3.10+)
print("\n--- 11. match-case ---")
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")

# Simple calculator with match-case
op = "+"
p, q = 10, 5
match op:
    case "+":
        print("Result:", p + q)
    case "-":
        print("Result:", p - q)
    case "*":
        print("Result:", p * q)
    case "/":
        print("Result:", p / q)
    case _:
        print("Invalid operator")