# Square Pattern
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# Increasing Triangle Pattern
n = 5
for i in range(n):
    for j in range(i+1) :
        print("*", end=" ")
    print()

# Decreasing Triangle Pattern
n = 5
for i in range(n):
    for j in range(i, 5):
        print("*", end=" ")
    print()

# Right Sided Triangle
n = 5
for i in range(n):
    for j in range(i, 5):
        print("", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()

