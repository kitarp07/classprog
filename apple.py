# N students take K apples and distribute them among each other evenly. The remaining ( the undivisible)
# part remains in the basket. how many apples will each single student get?
# How many apples will remain in the basket? The program reads the number N and K.

N = int(input("enter the number of students in the class: "))
K = int(input("tnter the number of apples: "))
apples_get = K//N
remaining_apples = K%N
print(f'Each student got {apples_get}')
print(f'The remaining number of apples are {remaining_apples}')

