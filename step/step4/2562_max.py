#####

max = 0
idx = 0

for i in range(9):
    num = int(input())

    if num > max:
        max = num
        idx = i + 1
    
print(max)
print(idx)