#Uses a for loop to iterate over numbers from 1 to 50.
for i in range (1,51):
    print(i)

#Calculates the sum of all integers in this range.
num=int(input("Enter any number - "))
sum=0
for i in range(num+1):
    sum+=i
print(sum)