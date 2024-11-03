from user_interface import start_interactive_session
from latex_utils import load_or_create_latex
from data_fetcher import update_publications

def main():
    # Start the interactive session for user input
    user_data = start_interactive_session()
    
    # Load an existing LaTeX file or create a new one based on user input
    latex_document = load_or_create_latex(user_data)
    
    # Fetch and update publications if necessary
    updated_latex = update_publications(latex_document, user_data['name'])
    
    # Save the updated LaTeX document
    with open('outputs/updated_cv.tex', 'w') as file:
        file.write(updated_latex)

if __name__ == "__main__":
    main()