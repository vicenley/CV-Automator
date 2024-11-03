def get_user_decision():
    """
    Prompt the user to decide if they want to load an existing CV or create a new one.
    Returns the user's decision as a string.
    """
    print("Do you want to load an existing CV or create a new one?")
    print("1: Load existing CV")
    print("2: Create new CV")
    decision = input("Enter your choice (1 or 2): ")
    return decision

def get_file_path():
    """
    Asks the user for the file path to an existing CV.
    Returns the path as a string.
    """
    path = input("Please enter the path to your existing CV: ")
    return path

def collect_basic_information():
    """
    Collects basic personal information for creating a new CV.
    Returns a dictionary with the collected data.
    """
    print("Please enter your basic information for the new CV.")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    return {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone
    }

def collect_additional_details():
    """
    Engages the user to input additional details like research interests, hobbies, and technical skills.
    Returns a dictionary with the additional details.
    """
    print("Please enter additional details for your CV.")
    research_interests = input("Research Interests: ")
    hobbies = input("Hobbies: ")
    technical_skills = input("Technical Skills: ")
    return {
        'research_interests': research_interests,
        'hobbies': hobbies,
        'technical_skills': technical_skills
    }

def confirm_details(details):
    """
    Displays the details entered by the user and asks for confirmation to proceed.
    Returns True if the user confirms, False otherwise.
    """
    print("\nPlease confirm the details you entered:")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")
    confirmation = input("Is this information correct? (yes/no): ")
    return confirmation.lower() == 'yes'