# --- HIGHER ORDER FUNCTIONS --------- 

#    -------- map() ,-------- filter(), ----------- reduce()-----------

# num = [1,3,4,6,7,5,6,10]

# def square(x):
#     return x*x

# new_num = [x for x in range(26)]
# print(new_num)
# print("-------------------------")
# newlist = [x for x in range(10)]

# print(newlist)

# print("-------------------------")

# mappedNum = list( map(lambda x: x*2,num))

# print(square(list([x for x in range(8)])))
# print(num[0],range(num[0],len(num)))
# print(mappedNum)

#------------------------filter---------------------

integers = [1,3,4,5,6,7,7,8,8,6,3,2]

num = list( filter( lambda x: x % 2 == 0,integers))

print(num)
#-------------------------- reduce() -------------------------
from functools import reduce

nums = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, nums)
print(total)
