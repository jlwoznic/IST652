# 
# Subject: Lab Problem 3
# Author: Joyce Woznica
# Date: 4/22/2020
#
# Problem 1

def fred(): 
   print("Zapped") 
def jane(): 
 	   print("ABCdef") 
jane() 
fred() 
jane() 
print("jane")


# Problem 2
# Compute Pay
def computepay(rate, hours):
    if not (isinstance(rate, str) or isinstance(hours, str)):
        if int(hours) or int(rate) or float(hours) or float(rate):
            if float(hours) > 40:
                grosspay = 40*(float(rate)) + (float(hours)-40)*(1.5*float(rate))
            else:
                grosspay = float(hours)*float(rate) 
        return grosspay
    else:
        print("Invalid inputs.")

computepay(40, 10)
computepay(45, 15)
computepay(41.23, 11)
computepay('six', 12.50)
