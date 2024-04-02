# --------------------- Welcome to GradCalc! --------------------------
# This program is a small project I created to determine graduation date for
# adults continuing their education. All others I found online were based
# on either age or year of high school graduation. Neither of those were any
# help to me. I just wanted to make something useful that would also serve as
# practice. Error control for all possible user entries has not yet been
# incorporated. Enjoy!

# GradCalc v 1.0
# copyright 2024
# James V Greene dba JaVerno Systems

import datetime
from datetime import datetime


# Welcome message to GradCalc prompting user to choose Associate or Bachelor.
def welcome_message():
    print("Welcome to GradCalc!")
    print("Please choose your degree:")
    print("1. Associate")
    print("2. Bachelor")
    degree_choice = input("Enter your choice (1 or 2): ").strip()
    if degree_choice in ["1", "2"]:
        return degree_choice
    else:
        print("Invalid input. Please enter 1 or 2.")


# If Associate is chosen total credits = 60. If Bachelor is chosen total credits = 120.
def get_degree_weight(degree_choice):
    if degree_choice == "1":
        return 60
    elif degree_choice == "2":
        return 120
    else:
        print("Invalid input. Please enter 1 or 2.")  # Limit input to '1' or '2'


# Prompt user for number of weeks per term insuring that the input is a positive integer that
# does not exceed 52. If error, prompt user to re-enter input.
def get_weeks_per_term():
    while True:
        try:
            weeks_per_term = int(input("Enter the number of weeks per term: "))
            if weeks_per_term <= 0 or weeks_per_term > 52:
                raise ValueError("Please enter a positive integer less than or equal to 52.")
        except ValueError as e:
            print(e)
        else:
            break
    return weeks_per_term


# Prompt user for number of hours taken per term insuring that the input is a positive integer.
def get_hours_per_term():
    while True:
        try:
            hours_per_term = int(input("Enter the number of hours you will take per term: "))
            if hours_per_term <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    return hours_per_term


# Prompt user for number of terms they expect to take each year.
# Input must not be greater than 52 divided by weeks_per_term.
# If error, prompt user to re-enter input.
def get_terms_per_year(weeks_per_term=None):
    while True:
        try:
            terms_per_year = int(input("Enter the number of terms you will attend per year: "))
            if terms_per_year <= 0 or terms_per_year > (52 / weeks_per_term):
                raise ValueError("Please enter a positive integer less than or equal to " + str(52 // weeks_per_term))
            break
        except ValueError as e:
            print(e)
    return terms_per_year


# Get hours currently completed from user input. Must be >= 0.
# Subtract from degree_weight
def get_hours_completed():
    hours_completed = input("Enter the number of hours already completed: ")
    try:
        hours_completed = int(hours_completed)
        if hours_completed < 0:
            raise ValueError
        return hours_completed
    except ValueError:
        print("Invalid input. Please enter a positive integer.")


# Create a variable called remaining_hours that is the degree_weight minus hours_completed
def get_remaining_hours(degree_weight=None, hours_completed=None):
    remaining_hours = max(0, degree_weight - hours_completed)  # Ensure remaining_hours is not negative
    return remaining_hours


# Determine graduation date based on current month/year + (remaining_hours / hours_per_term)
# Output expected graduation in the form of MMMM yyyy
def get_graduation_date(remaining_hours, hours_per_term, terms_per_year):
    if remaining_hours <= 0:
        # Required hours have already been completed
        return "Eligible for graduation or already graduated."
    # Calculate the total number of terms needed to complete the remaining hours
    total_terms_needed = remaining_hours / hours_per_term

    # Calculate how many years and terms this corresponds to
    years_needed = int(total_terms_needed / terms_per_year)
    remaining_terms = total_terms_needed % terms_per_year

    # Convert the remaining terms to months (approximation)
    months_needed = int((remaining_terms / terms_per_year) * 12)

    # Calculate the graduation date by adding the years and months to the current date
    current_year = datetime.now().year
    current_month = datetime.now().month

    graduation_year = current_year + years_needed
    graduation_month = current_month + months_needed

    # Adjust for overflow in months
    if graduation_month > 12:
        graduation_year += 1
        graduation_month -= 12

    # Assuming graduation day is at the end of the graduation month
    graduation_date = datetime(graduation_year, graduation_month, 1)

    return graduation_date


# Output return variables from previous functions and print each on a new line.
def output_results(degree_weight, weeks_per_term, hours_per_term,
                   terms_per_year, hours_completed,
                   remaining_hours, graduation_date):
    print(f"Total credits required for graduation: {degree_weight}")
    print(f"Weeks per term: {weeks_per_term}")
    print(f"Hours expected per term: {hours_per_term}")
    print(f"Terms expected per year: {terms_per_year}")
    print(f"Hours completed: {hours_completed}")
    print(f"Hours expected per year: {hours_per_term * terms_per_year}")
    print(f"Hours remaining: {remaining_hours}")
    # Adjust for completion of required credits
    if isinstance(graduation_date, datetime):
        formatted_graduation_date = graduation_date.strftime('%B %Y')
        print(f"Expected graduation: {formatted_graduation_date}")
    else:
        print(f"Expected graduation: {graduation_date}")


# Main function to call all other functions
def main():
    degree_choice = welcome_message()
    degree_weight = get_degree_weight(degree_choice)
    weeks_per_term = get_weeks_per_term()
    hours_per_term = get_hours_per_term()
    terms_per_year = get_terms_per_year(weeks_per_term)
    hours_completed = get_hours_completed()
    remaining_hours = get_remaining_hours(degree_weight, hours_completed)
    formatted_graduation_date = get_graduation_date(remaining_hours, hours_per_term, terms_per_year)
    output_results(degree_weight, weeks_per_term, hours_per_term, terms_per_year, hours_completed,
                   remaining_hours, formatted_graduation_date)


# Call main function
main()
