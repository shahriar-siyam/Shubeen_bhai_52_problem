n=int(input())

for i in range(n):
    k=int(input())
    d = []
    print(f"Case {i+1}:",end=' ')
    for j in range(1,k+1):
        if k%j==0:

            d.append(j)

    print(*d,end='')
    print("")

