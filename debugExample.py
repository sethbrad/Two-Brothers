numbers = []

for i in range(0, 50):
    numbers.append(i)

for i in range(0, 50):
    if i % 3 == 0:
        print(numbers[i // 3])