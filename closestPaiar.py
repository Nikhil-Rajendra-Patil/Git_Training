def closestPair(List, N):
    for i in range(N-1):
        for j in range(i+1,N):
            if abs(List[i]-List[j]) < diff:
                diff = abs(List[i]-List[j])
    return diff

N = int(input())
List = []
for i in range(N-1):
    ele = int(input())

Result = closestPair(List, N)
print(Result)