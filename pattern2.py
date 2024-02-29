n = int(input("Enter the number of rows: "))
k = 0
for i in range(n, 0, -1):
    k += 1
    for j in range(1, i+1):
        print(k, end=" ")
    print()
