# Self made but inefficient; can only handle small n < 100 going beyond may lead to inaccuracies

import random

numbers = [random.randint(0, 100) for i in range(5)]
composite = []
prime = []

for i in numbers:
    if i == 0:
        print("0 is neither prime nor composite")
    elif i == 2 or i == 3 or i == 5 or i == 7 or i == 11 or i == 13:
        prime.append(i)
    elif i == 1 or i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0 or i % 13 == 0:
        composite.append(i)
    else:
        prime.append(i)

print(numbers)
print(f"Composite Numbers: {composite}")
print(f"Prime Numbers: {prime}")
