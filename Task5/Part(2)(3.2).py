#Functions
def sum_two_values(x,y):
    print("Summing two values")
    return x+y
sum = sum_two_values(3,4)
print(sum)
#Output: 7

#Returning many values
def sum_and_product(x,y):
    return x+y,x*y
sp = sum_and_product(3,4)
print(sp)

#Lambda functions
f = lambda x: x**2
print("Lambda Function" ,f(2))
