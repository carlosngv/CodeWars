""" 
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times. 
"""

# First solution

def find_it(seq):
    dic = {}
    for number in seq:
        if str(number) not in dic:
            dic[str(number)] = 1
        else:
            dic[str(number)] += 1
    for k, v in dic.items():
        if v % 2 != 0:
            return int(k)

# Second solution

def find_it2(seq):
    for n in seq:
        if seq.count(n) % 2 != 0:
            return n

if __name__ == '__main__':
    seq = [1,2,1,1,2,2,2,4]
    print(find_it(seq))
    print(find_it2(seq))