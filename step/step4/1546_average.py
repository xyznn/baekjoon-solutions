N = int(input())
scores = list(map(int, input().split()))

x = max(scores)

for i in range(len(scores)):
    scores[i] = scores[i] / x*100

print(sum(scores)/len(scores))