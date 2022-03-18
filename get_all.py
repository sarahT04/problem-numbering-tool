

# This is tryout to get the columns I want
"""
1  4  7
2  5  8
3  6
"""

my_dict = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
           }

divide_by = 3
nums = list(my_dict.keys())
length = round(len(nums) / divide_by)

s = ''
for i in range(length + 1):
    j = i
    for c in range(1, divide_by + 1):
        try:
            s += str(my_dict[nums[j]]).ljust(3)
            j += length + 1
        except IndexError:
            break
    s += '\n' 
print(s)


"""
index has to be:
0 + 3 + 6
1 + 4 + 7
2 + 5
"""