from user_interface import get_user_decision, get_file_path, collect_basic_information, collect_additional_details, confirm_details
from latex_utils import load_latex_from_file, create_new_latex_template, update_latex_document, save_latex_to_file
from data_fetcher import update_cv_data

def main():
    decision = get_user_decision()

    if decision == '1':
        file_path = get_file_path()
        latex_content = load_latex_from_file(file_path)
        parsed_data = parse_latex_content(latex_content)  # Assuming this function is implemented to extract data
        name = parsed_data.get('name')
    else:
        basic_info = collect_basic_information()
        if not confirm_details(basic_info):
            print("Please restart the process.")
            return
        latex_content = create_new_latex_template()
        name = basic_info['first_name'] + ' ' + basic_info['last_name']
        latex_content = update_latex_document(latex_content, basic_info)  # Assuming this handles adding basic info to template

    # Fetch new data based on the name extracted or provided
    cv_data = update_cv_data(name)

    # Collect additional user-provided information
    additional_details = collect_additional_details()
    if not confirm_details(additional_details):
        print("Please restart the process.")
        return

    # Update the CV with new data and additional details
    latex_content = update_latex_document(latex_content, cv_data)
    latex_content = update_latex_document(latex_content, additional_details)

    # Save the updated LaTeX CV
    save_latex_to_file(latex_content, f'outputs/{name.replace(" ", "_")}_CV.tex')
    print(f"CV updated and saved successfully as {name.replace(' ', '_')}_CV.tex in the outputs directory.")

if __name__ == "__main__":
    main()