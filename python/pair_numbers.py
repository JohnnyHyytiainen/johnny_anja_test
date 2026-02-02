numbers = [1, 3, 5, 3, 7, 5]
duplicates = []

for num in range(len(numbers)):
    for i in range(num + 1, len(numbers)):
        if numbers[num] == numbers[i] and numbers[num] not in duplicates:
            duplicates.append(numbers[num])
print(duplicates)