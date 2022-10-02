

 # Q.2) Write a Python program to triple all numbers of a given list of integers. Use Python map.

#sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers: [3, 6, 9, 12, 15, 18, 21]   




lst = [1, 2, 3, 4, 5, 6, 7]


result = map(lambda v: v + v + v, lst) 

print("Triple of list numbers:")

print(list(result))