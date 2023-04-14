##day-9-start

##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]






programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    401: "Error code in computer.",
}

print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
print(programming_dictionary[401])



programming_dictionary["Loop"] = "The action of doing omething over and over again"

print(programming_dictionary)

empty_dictionary = {}
empty_dictionary["qwe"] = "Great"
print(empty_dictionary)

##programming_dictionary = {}
##print(programming_dictionary)

print(programming_dictionary["Bug"] )
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"] )


for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


bike_start = {}
bike_start["process"]= "get keys"
print(bike_start)


##Exercise 1 - Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score >80:
        student_grades[student] = "Exceeds Expectations"
    elif score >70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)



##PRACTICE
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score >80:
        student_grades[student] = "Exceeds Expectations"
    elif score >70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)


##nesting ex
travel_log = {
  "France": {
      "cities_visited": ["Paris", "Lille", "Dijon"],
             "total_visits": 12
             },
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
print(travel_log)



travel_log = [
    {
        "'country": "France",
        "cities visited": ["Paris", "Lille", "Dijon"],
        "Total_visits": 12
        },
    {
        "country":"Germany",
        "Capital":"Berlin",
        "Top Locations to visit": ["Berlin", "Hamburg", "Stuttgart"],
        "Visa on Arrival": "Depends",
        "Total_visits" : 3
        }
]
print(travel_log)






##Exercise 2 - Dictionary in List


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
##travel_log["Loop"] = "The action of doing something over and over again."


def add_new_country(country_visited , times_visited ,  cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
    

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


#FINAL PROJECT

##blind-auction-start
from Art_Day9 import logo
print(logo)

#HINT: You can call clear() to clear the output in the console.

bids={}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of $ {bid_amount}")
        

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?:  $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? type 'yes' or 'no'? ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        pass
    








