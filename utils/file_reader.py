# utils/file_reader.py

def read_file(file_path):
    """
    Reads the content of a text-based file using UTF-8 encoding.

    Args:
        file_path (str): The path to the file that needs to be read.

    Returns:
        str: The content of the file if successful, or an error message if reading fails.
    """
    try:
        # Attempt to open and read the file in read mode with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        # If an error occurs (e.g., file not found, permission error), return a string with the error info
        return f"[Error reading file: {e}]"