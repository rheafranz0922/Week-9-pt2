# Function to get thenon empty in string input from a user.
def get_non_empty_string(prompt):
    """Prompt the user until they enter a non-empty string."""
    user_input = ""
    while not user_input.strip(): # Keep  asking the input
        user_input = input(prompt).strip()
        if not user_input:
            print("Input is empty and please try again.")
    return user_input

# A function is to gather the data by helping a function
def get_positive_integer(prompt):
    """Prompt the user until they enter a valid positive integer."""
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid positive number.")

def collect_user_data():
    fullname = get_non_empty_string("Enter your Fullname: ")
    age = get_positive_integer("Enter your age: ")
    favorite_color = get_non_empty_string("Enter your favorite color: ")
    favorite_subject = get_non_empty_string("Enter your favorite subject: ")
    pet = get_non_empty_string("What is your favorite pet")
    
    return fullname, age, favorite_color, favorite_subject, pet

# Display the data in a format way.
def display_user_data(fullname, age, color, favorite_subject, pet):
    print("\n..... User Data.....")
    print(f"Name: {fullname}")
    print(f"Age: {age}")
    print(f"Favorite Color: {color}")
    print(f"Favorite Subject: {favorite_subject}")
    print(f"Favorite Pet: {pet}")


# Main program
def main():
    name, age, color, subject, pet = collect_user_data()
    display_user_data(name, age, color, subject, pet)

main()