# Coded triangle numbers

import math
file_names = open("problem042_names.txt","r")

total_names = sorted(file_names.read().replace('"','').split(','))

alphabet = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}

count = 0
for index, item in enumerate(total_names):
    value = 0
    for index1, item1 in enumerate(list(item)):
        value += alphabet[item1.lower()]
    if value * 2 == int(math.sqrt(value * 2)) * (int(math.sqrt(value * 2)) + 1):
        count += 1

print(count)