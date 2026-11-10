#first_practice
a = [1 ,2 ,3 ,4 ,5] 
for m in a:
    print(m) 

print('*' * 40) 
#second_and_third_practice:
m1 = ["mitsubishi","hyundai","honda","toyota"] 
print(m1[0])
print(m1[3]) 
print(len(m1)) 

print("*"  * 40) 
#4th_and_5th_practice: 
numbers = [1 , 2, 3] 
numbers.append(4) 
print(numbers) 
del numbers[1] 
print(numbers) 
print("*"  * 40)
#6th_practice:
h1 = [2,4,6,8]
print(f"{[h1[0] + h1[1]]}")
#7th_practice:? 
print("*"  * 40) 
#8th_practice:
a1 = [] 
b1 = [3,4,6] 
a1.append(b1) 
print(a1) 

print("*"   * 40) 

#9th_practice:
k1 = [3, 4, 6, 8] 
print(f"{[k1[0] + k1[1] + k1[2] + k1[3]]}") 
print("*"    * 40) 
#10th_practice:
k63 = []
num = [5, 15, 8, 20, 3] 
for n in num:
    if n > 10:
        k63.append(n) 

print(k63) 
print("*"    * 40) 
#11th_practice:
k22 = ["los angeles","dallas","new york"] 
k23 = ["paris","london"] 
k22.append(k23) 
print(k22) 
#conditionings:
print( "*"    * 40)
a47 = []; b48 = []
a23 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for m16 in a23:
    if m16 % 2 == 0:
        a47.append(m16)
    else:
        b48.append(m16)

print(a47)
print(b48)
#dictionaries:
print("*"     * 40)
a46 = {'name':"lamborghini"}
print(a46['name'])
