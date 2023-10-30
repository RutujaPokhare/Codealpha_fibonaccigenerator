def fibonacci():
    x,y = 0,1
    while True:
        yield x
        x,y = y,x+y

n = int(input("Enter the number of fibonacci series you want to generate: "))
print("first",n,"Fibonacci numbers:")
result = fibonacci()
for i in range(n):
    print(next(result),end=" ")
