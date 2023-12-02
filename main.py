import csv

numbers = list(map(str, list(range(1, 10))))
letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] + list(map(str, list(range(1, 10))))
l = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
combined = list(zip(numbers, l))


total = 0
hashmap = {}

with open('file.csv', 'r') as file:
    text = csv.reader(file)
    for line in text:
        for letter in letters:
            if letter in line[0]:
                positionf = line[0].find(letter)
                positionb = line[0].rfind(letter)
                if positionb != positionf:
                    hashmap[positionf] = letter
                    hashmap[positionb] = letter
                else:
                    hashmap[positionf] = letter
        first_to_calculate = hashmap[min(hashmap.keys())]
        second_to_calculate = hashmap[max(hashmap.keys())]
        if first_to_calculate in l:
            for i in combined:
                if first_to_calculate in i:
                    first_to_calculate = i[0]
        if second_to_calculate in l:
            for i in combined:
                if second_to_calculate in i:
                    second_to_calculate = i[0]
        res = (str(first_to_calculate) + str(second_to_calculate))
        total += int(res)
        hashmap = {}
    print(total)
