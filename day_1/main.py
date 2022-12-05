numbers = []
maths = []
total = 0
arr_counter = 1
with open("elf_calories.txt", 'r') as file:
    numbers = file.readlines()
print(numbers)
for number in numbers:
    if number.strip('\n') != '' and arr_counter < len(numbers):
        total += int(number)
        pass
    elif arr_counter == len(numbers):
        total += int(number)
        maths.append(total)
    else:
        maths.append(total)
        total = 0
    arr_counter += 1

print(maths)