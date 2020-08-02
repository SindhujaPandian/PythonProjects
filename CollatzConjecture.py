n = int(input("Enter the number  : "))
steps = 0
while n!=1:
    if n%2 == 0 :
        n = n//2
        steps+=1
    else:
        n = 3*n +  1
        steps +=1
print(steps)
