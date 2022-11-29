#!/usr/bin/python3
count = 0;
for num in range(100):
        print("{0}".format(num), end='')
        count = count + 1
        if count < 100:
            print(", ", end='')
            count = count + 1
