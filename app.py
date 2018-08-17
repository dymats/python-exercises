# 1. As a valued customer at the Bank of Honolulu, you make a deposit of $1000. Your savings account balance prior to the deposit has an amount of $8000. Calculate the new savings account balance. Print the new savings account balance and concatenate the dollar sign.
original_bal = 8000
deposit = 1000
def add(num1, num2):
    return num1 + num2
new_bal = add(original_bal, deposit)
print('$' + str(new_bal))
 
# 2.You need to pay taxes on the $500 cash prize that you won to the IRS ( The tax rate is 30%). Calculate the tax amount and subtract this from your savings balance. Print the updated savings account balance and concatenate the dollar sign.
prize = 500
tax_rate = .30
savings_bal = 9000
def product(num1, num2):
    return num1 * num2    
tax_amount = product(prize, tax_rate)
def difference(num1, num2):
    return num1 - num2
new_bal = difference(savings_bal, tax_amount)
print('$' + str(new_bal))    
    
# 3. The savings account accrues an annual interest rate of 2%. Calculate the interest earned for the first quarter of 2018, using the original account balance from Question 1. Print the interst earned in the first quarter and concatenate the dollar sign.
savings_bal = 9000
quarterly_interest = .005
def multiply(num1, num2):
    return num1 * num2
interest = multiply(savings_bal, quarterly_interest) 
print ('$' + str(interest)) 

# 4. Function add
# Create a function that will take two parameters named num1 and num2. This function will add two numbers. Print your result.
def addition(num1, num2):
    'sum up any two numbers'
    sum = num1 + num2
    return sum
addition(3,5)
add_up = addition(3,5)
print(add_up)    

# 5. Function subtract
# Create a function that will take two parameters named num1 and num2. This function will subtract two numbers. Print your result.
def subtract(num1, num2):
    'subtract two numbers'
    sum = num1 - num2
    return sum
subtract(5,3)
sum_up = subtract(5,3)  
print(sum_up)

# 6. Function add-then-subtract
# Create a function that will take in three parameters named num1, num2 and num3. The function will sum up the first two parameters (num1 and num2) and subtract it from the third parameter (num3). Please use your previous functions (i.e. add or subtract) for this exercise. Print your result.
def add_subtract(num1, num2,num3):
    'add first two numbers and subtract from third number'
    sum = (num3 - (num1 + num2))
    return sum     
sum = add_subtract(1,2,3)
print(sum)

# 7. Function shoe size
#  Create a function that will take in a parameter named inches. This function will convert inches to centimeters(cm). Print your result. 
def convert(inches, centimeters):
    'convert inches to centimeters'
    sum = inches * centimeters
    return sum

convert(1,2.45)
sum = convert(1,2.45)
print(sum)    
# 8. Create a function that will take in a parameter named cel. The function will convert Celsius into Fahrenheit. Print your result.
def convert_degree(cel, fahrenheit):
    'convert cel to fahrenheit'
    sum = cel * fahrenheit
    return sum
sum = convert_degree(2,33.8)
print(sum)  

# 9. Function all caps
#  Create a function that will take in a parameter named str. This function will capitalize all the letters in the string. Print your result. 
def all_caps(str):
    return str.upper()
print(all_caps('jarren'))  

# 10. Function one cap
#  Create a function that will take in a parameter named str. The function will capitalize only the first letter in the string. Print your result.
def first_letter(str):
    return str.capitalize()
print(first_letter('jarren')) 

# 11. Use the extend method to combine the following lists together. Print your result.

east_side = ['Biggie', 'Nas', 'Wu-Tang Clan']
west_side = ['Tupac', 'Dre', 'Snoop']
east_side.extend(west_side)
print('extended list : ',east_side)

# 12. Use the clear method to remove all items from the following list. If you are using Python 2 or 3.2, use the del operator instead. Print your result.

haters = ['Keyshia Cole', 'Wendy Williams', '50 Cent', 'Lil Kim']
del haters[0:len(haters)]











