In Python, the function is a block of code defined with a name.
We use functions whenever we need to perform the same task multiple times without writing the same code again. 
It can take arguments and returns the value.



for i in range(1, 15):                (in-built function)
    print(i, end=' ')
# Output 1 2 3 4 5 6 7 8 9


# function
def message():
    print("Welcome to Pythone")

# call function using its name
message()                          (output Welcome to Python)




# function
def calculator(a, b):
    add = a + b                                               
    # return the addition
    return add

# call function
# take return value in variable
res = calculator(20, 5)

print("Addition :", res)
# Output Addition : 25
