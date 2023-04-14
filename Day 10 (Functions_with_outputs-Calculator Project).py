##day-10-start

##Functions with outputs

def format_name(f_name ,l_name):
    """Take a first name and last name
and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "you didn't provide valid inputs."
        
    formatted_f_name = f_name.upper()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
##bread = format_name("rubber sheet paTTO sound","nayaee kazichellakkel")
##print(bread)

print(format_name(input("What is your first name? "), input("What is your last name? ")))



##Exercise 1 - Days in Month
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return  False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
##    if month > 12 or month < 1:
##        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
        
          
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)



##FINAL 
##calculator-start

from Art_Day10 import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

##calculation_finished = False
##while not calculation_finished:
##
##    num1 = int(input("What's the first number?:\n  "))
##
##    for symbol in operations:
##        print(symbol)
##    operation_symbol = input("Pick an operation from the line above:\n")
##    num2 = int(input("What's the second number?:\n"))
##    calculation_function = operations[operation_symbol]
##    first_answer = calculation_function(num1, num2)
##
##    print( f"{num1} {operation_symbol} {num2} = {first_answer}")
##    
##    should_continue = input(f"Type 'y' to continue calculating with {first_answer}, or  type 'n' to exit.:  ")
##    if should_continue == "no":
##        calculation_finished = True
##        print("Thank you. Don't forget to come again for your next calculation.Bye")
##    elif should_continue == "yes":
##        operation_symbol = input("Pick another operation: ")
##        num3 = int(input("What's the next number?: "))
##        calculation_function = operations[operation_symbol]
##        second_answer = calculation_function(calculation_function(num1, num2), num3)
##        print( f"{first_answer} {operation_symbol} {num3} = {second_answer}")
##        


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print( f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or  type 'n' to start a new calculation.:  ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()



            
    
    

