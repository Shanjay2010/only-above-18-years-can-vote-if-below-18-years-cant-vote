def check_voting_eligibility(age):
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("Sorry, you are not eligible to vote. You must be 18 years or older.")

# Get the user's age as input
user_age = int(input("Enter your age: "))

# Check eligibility
check_voting_eligibility(user_age)
