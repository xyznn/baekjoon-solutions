a, b, c = map(int, input().split())

if a == b and b == c:
    prize = 10000 + a*1000
elif a == b or a == c:
    prize = 1000 + a*100
elif b == c:
    prize = 1000 + b*100
else:
    d = max(a, b, c)
    prize = d*100

print(prize)