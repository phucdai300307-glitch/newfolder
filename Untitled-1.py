
a = list(map(int, input().split()))
s = 0

for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] < a[j]:
            b = a[i] * (j - i + 1)
            if b > s:
                s = b
        else :
          break

print(s)
