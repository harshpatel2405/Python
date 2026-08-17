'''
Names and Salary Combination

employees = [
    ("Harsh", 25000),
    ("Rahul", 28000),
    ("Amit", 18000),
    ("Neha", 52000),
    ("Priya", 32000)
]

Create a function get_high_salary_employees(employees).

Requirements:

Use filter() with lambda to select employees earning more than ₹30,000.
Use map() with lambda to extract only their names.
Return the names.

Expected Output:

["Neha", "Priya"]
'''


def get_high_salary_employees(employee):
    salaried_data = list(filter(lambda x: x[1] > 30000, employees))
    names = list(map(lambda x: x[0], salaried_data))
    return names


employees = [("Harsh", 25000),
             ("Rahul", 28000),
             ("Amit", 18000),
             ("Neha", 52000),
             ("Priya", 32000)
             ]

ans = get_high_salary_employees(employees)
print(ans)

'''
Online Shopping Cart 🔥
Create a function: calculate_cart(prices)

Given:
prices = [499, 1200, 750, 2500, 300, 1800]

Perform these operations:

Use filter() to remove products costing less than ₹500.
Use map() to apply a 20% discount.
Use another filter() to keep only products whose discounted price is greater than ₹500.
Use map() to round the prices to integers.
Return the final list.
'''

'''
3. Number Processing Pipeline 🔥

Create a function:  process_numbers(numbers)

Given:

numbers = [12, 5, 18, 7, 24, 31, 40, 9, 16]

Perform the following:

Filter numbers greater than 10.
Filter only even numbers.
Square those numbers.
Add 10 to every squared value.
Return the final list.
'''

