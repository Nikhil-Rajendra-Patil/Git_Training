input_string = input()

count = 0
vowels = 'aeiouAEIOU'

for i in input_string:
    if i in vowels:
        count += 1

print(count)