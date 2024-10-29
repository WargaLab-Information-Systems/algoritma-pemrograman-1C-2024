# for i in range (1,4):
#     print(f"Loop luar i = {i}")

#     for j in range (1,4):
#         print(f"Loop dalam j {j}")


# a = 24
# b = 36

# while b!= 0:
#     a,b = b, a % b

# print(f"FPB nya adalah : {a}")


# n = 100
# a = 0
# b = 1
# print("bilangan Fibonacci hingga ", n )
# while a <= n:
#     print(a, end=" ")
#     a,b = b, a + b


n = 5
for i in range(1, n+1):

    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1, i+1):
        print(k, end=" ")
    print()