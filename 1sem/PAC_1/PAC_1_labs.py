import argparse
import random

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true') # on/off flag

args = parser.parse_args()
n = int(args.count)

#  1 lab task
value = []
for _ in range(n + 1):
    value.append(random.random())
print(type(value[0]))
for i in range(len(value)):  
    for j in range(0, n - i):  
        if value[j] > value[j + 1]:  
            value[j], value[j + 1] = value[j + 1], value[j]  
print(value) 

# 2 lab task
pascal = []
for i in range(n):
    z = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            z[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    pascal.append(z)
j = 0
for i in pascal:
    print(' '*len(pascal[j:]), i)
    j += 1