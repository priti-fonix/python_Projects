'''
favmov=[]
mov1 =input('enter your 1st fav movies')
mov2 =input('enter your 2nd fav movies')
mov3 =input('enter your 3rd fav movies')
favmov.append(mov1)
favmov.append(mov2)
favmov.append(mov3)
print(favmov)'''

#-----------------------------palindrome brute force-----------------
'''
lst=[]
i1 = input("enter the items of the list")
i2 = input("enter the items of the list")
i3 = input("enter the items of the list")
i4 = input("enter the items of the list")
lst.append(i1)
lst.append(i2)
lst.append(i3)

lst.append(i4)

lstc = lst.copy()
lstc = lstc.reverse()

if lstc == lst :
    print(' palindrome')
else:
    print('not palindrome')
'''

#---------------dict---------------------------------------------
dict = {
    "name": "priti",
    "subject" :{
        "phy":45,
        "chem":89,
        "math":100
    }
}
# dict = set(dict)

print(dict["name"])

set = {
    "radha",1,"priti"
}
print(set)
