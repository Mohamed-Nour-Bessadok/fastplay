def read_file(file_path):
    """Reads a text file and returns its content as a string."""
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except IOError:
        print(f"Error: Could not read the file at {file_path}.")
        return None


def extract_competition_results(file_path, start_keyword, end_keyword):
    """Extracts the competition results section from the text."""
    
    text = read_file(file_path)
    start_index = text.find(start_keyword)
    if start_index == -1:
        print("Error: Start keyword not found in the text.")
        return None

    end_index = text.find(end_keyword, start_index)
    if end_index == -1:
        print("Error: End keyword not found in the text.")
        return None

    section = text[start_index:end_index]
    return section
