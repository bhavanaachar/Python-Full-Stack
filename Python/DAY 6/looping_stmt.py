# 1. for loop with range
print("--- 1. for with range ---")
for i in range(5):
    print(i, end=" ")
print()

for i in range(2, 11, 2):          # start, stop, step
    print(i, end=" ")
print()

for i in range(5, 0, -1):          # countdown
    print(i, end=" ")
print()

# 2. for over list and string
print("\n--- 2. for over list / string ---")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

for ch in "Python":
    print(ch, end="-")
print()

# 3. Multiplication table
print("\n--- 3. Table of 5 ---")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# 4. Sum of 1 to 100
print("\n--- 4. Sum 1 to 100 ---")
total = 0
for i in range(1, 101):
    total += i
print("Sum =", total)

# 5. Factorial
print("\n--- 5. Factorial of 5 ---")
fact = 1
for i in range(1, 6):
    fact *= i
print("5! =", fact)

# 6. while loop
print("\n--- 6. while loop ---")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# 7. Reverse a number (while)
print("\n--- 7. Reverse a number ---")
number = 12345
rev = 0
while number > 0:
    digit = number % 10
    rev = rev * 10 + digit
    number //= 10
print("Reversed:", rev)

# 8. Count digits
print("\n--- 8. Count digits ---")
n = 98765
digits = 0
while n > 0:
    n //= 10
    digits += 1
print("Digits:", digits)

# 9. break
print("\n--- 9. break ---")
for i in range(1, 10):
    if i == 5:
        print("Found 5, stopping")
        break
    print(i)

# 10. continue
print("\n--- 10. continue ---")
for i in range(1, 8):
    if i % 2 == 0:
        continue                   # skip even numbers
    print(i, end=" ")
print()

# 11. pass
print("\n--- 11. pass ---")
for i in range(3):
    if i == 1:
        pass                       # placeholder
    print("i =", i)

# 12. Loop else (prime check)
print("\n--- 12. Loop else ---")
target = 7
for i in range(2, target):
    if target % i == 0:
        print(target, "is not prime")
        break
else:
    print(target, "is prime")      # runs only if no break

# 13. Nested loops: star pattern
print("\n--- 13. Star pattern ---")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Number pyramid
print()
for i in range(1, 6):
    print(" " * (5 - i) + " ".join(str(j) for j in range(1, i + 1)))

# 14. Primes up to 50
print("\n--- 14. Primes up to 50 ---")
for num in range(2, 51):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
print()

# 15. FizzBuzz
print("\n--- 15. FizzBuzz ---")
for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 16. enumerate, zip, reversed
print("\n--- 16. enumerate / zip / reversed ---")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(index, color)

names = ["Asha", "Ravi", "Meena"]
scores = [88, 92, 79]
for name, score in zip(names, scores):
    print(name, "scored", score)

for c in reversed(colors):
    print(c, end=" ")
print()

# 17. while with break (guess the number)
print("\n--- 17. Guess the number ---")
secret = 42
guesses = [10, 80, 42]             # simulated guesses
attempt = 0
while attempt < len(guesses):
    guess = guesses[attempt]
    attempt += 1
    if guess < secret:
        print(f"Attempt {attempt}: {guess} is too low")
    elif guess > secret:
        print(f"Attempt {attempt}: {guess} is too high")
    else:
        print(f"Attempt {attempt}: {guess} is correct!")
        break

# Real interactive version (uncomment to try):
# while True:
#     guess = int(input("Guess the number: "))
#     if guess == secret:
#         print("Correct!")
#         break
#     print("Too low" if guess < secret else "Too high")