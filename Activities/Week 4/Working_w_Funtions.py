# Working with Functions

# Write a short program to create the two functions below.  
# Run your code a few times with different values.

# 1.  Create a function add_tax(amount, tax_rate) that accepts numeric values, amount and tax_rate,
#     and returns a new total amount with the tax amount included. 

def add_tax(amount, tax_rate):
    # need to check if tax is percent or float
    
    totalwTax = amount + amount*tax_rate
    return totalwTax


add_tax(10, .08)
add_tax(2000, 0.06)
add_tax(15000, 0.07)

# Note: that tax rate and tax amount are different.

# 2.  Define a function mean(a, b, c) that returns the mean of three numbers. 
#     Hint: Divide by 3.0 to get a float. 
#     Make sure that your answer only has 2 decimals.

def my_mean(a, b, c):
    avg = (a + b + c)/3.0
    # need to format to 2 decimal places
    return round(avg, 2)

my_mean(1, 2, 3)
my_mean(10,15,20)
my_mean(100, 275, 400)


# our group function
def add_tax(amount, tax_rate):
    if tax_rate > 1:
        tax_rate = tax_rate / 100
    total = amount + amount * tax_rate
    return total
    
amount = 5
tax_rate = 12
total = add_tax(amount, tax_rate)
print(f"Amount: {amount}\nTax Rate: {tax_rate}\nTotal: ${total}")

def mean(a, b, c):
    return float("{:.2f}".format((a+b+c)/3)) 

result = mean(5.3123, 4.21, 1.05)
print(result)

