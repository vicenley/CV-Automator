# user_interface.py

def start_interactive_session():
    # Collect user information or preferences
    print("Welcome to the CV Automator.")
    name = input("Please enter your name: ")
    file_path = input("Enter the path to your existing CV (leave blank to create a new one): ")
    return {'name': name, 'file_path': file_path}